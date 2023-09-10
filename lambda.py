import json
import boto3
import base64

#For error handling
import botocore

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    """A function to serialize target data from S3"""
    
    # Get the s3 address from the Step Function event input
    key = event['s3_key']
    bucket = event['s3_bucket']
    
    # Download the data from s3 to /tmp/image.png
    try:
        s3.Bucket(bucket).download_file(key, '/tmp/image.png')
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

    # We read the data from a file
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read())

    # Pass the data back to the Step Function
    print("Event:", event.keys())
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            
        }
    }

## classification

import json
import base64
import boto3

# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-2023-09-09-08-03-38-433"  # Replace with your SageMaker endpoint name
runtime = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    try:
        # Log the incoming event for debugging purposes
        print("Received event:", json.dumps(event))
        print("Event keys:", event.keys())

        # Check if "image_data" key exists in the event
        if "image_data" not in event:
            raise KeyError("Missing 'image_data' key in event")

        # Decode the image data
        image = base64.b64decode(event["image_data"])

        # Log that image decoding was successful
        print("Image decoding successful")

        # Instantiate a Predictor
        response = runtime.invoke_endpoint(EndpointName=ENDPOINT, ContentType='application/x-image', Body=image)
        inferences = response['Body'].read().decode('utf-8')
        event["inferences"] = [float(x) for x in inferences[1:-1].split(',')]

        # Log the inferences
        print("Inferences:", event["inferences"])

        # We return the data back to the Step Function
        return {
            'statusCode': 200,
            'body': {
                "image_data": event['image_data'],
                "s3_bucket": event.get('s3_bucket'),  # Use .get() to avoid KeyError if key is missing
                "s3_key": event.get('s3_key'),        # Use .get() to avoid KeyError if key is missing
                "inferences": event['inferences'],
            }
        }
    except Exception as e:
        # Log any exceptions that occur
        print("Error:", str(e))
        raise e  # Re-raise the exception for proper error handling


## low confidence Filteration

import json


THRESHOLD = .93


def lambda_handler(event, context):
    
    # Grab the inferences from the event
    inferences =event['inferences'] ## TODO: fill in
    
    # Check if any values in our inferences are above THRESHOLD
    meets_threshold =any(x>= THRESHOLD for x in inferences) ## TODO: fill in
    
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }

