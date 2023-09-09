"""
serializeImageData: a lambda function for pull an image from S3 and returning serializing data
"""
import json
import boto3
import base64


#For error handling
import botocore

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """A function to serialize target data from S3"""
    
    # Get the s3 address from the Step Function event input
    key = event['s3_key']
    bucket = event['s3_bucket']
    
    # Download the data from s3 to /tmp/image.png
    try:
    s3.Bucket(bucket).download_file(key, '/tmp/image.png')
    except botocore.exceptions.ClientError as e:
    error_code = e.response['Error']['Code']
    error_message = e.response['Error']['Message']
    
    if error_code == "404":
        print("The object does not exist.")
    else:
        print(f"An S3 error occurred: {error_code} - {error_message}")


    # We read the data from a file
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read())

    # Pass the data back to the Step Function
    print("Event:", event.keys())
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }
    }

## classification

import json
import sagemaker
import base64
from sagemaker.serializers import IdentitySerializer

# Fill this in with the name of your deployed model
ENDPOINT = "your_endpoint_name"  # Replace with your SageMaker endpoint name

def lambda_handler(event, context):
    # Decode the image data
    image = base64.b64decode(event['image_data'])  

    # Instantiate a Predictor
    predictor = sagemaker.predictor.Predictor(
        endpoint_name=ENDPOINT,
        serializer=IdentitySerializer("image/png"),  # Use the appropriate serializer
    )

    # Make a prediction
    inferences = predictor.predict(image_data)

    # We return the data back to the Step Function
    event["inferences"] = inferences.decode('utf-8')
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }


## low confidence Filteration

import json


THRESHOLD = .93


def lambda_handler(event, context):
    
    # Grab the inferences from the event
    inferences =event(['inferences']) ## TODO: fill in
    
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

