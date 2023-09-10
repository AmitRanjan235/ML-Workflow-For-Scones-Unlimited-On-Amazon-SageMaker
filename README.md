# Project: Build a ML Workflow For Scones Unlimited On Amazon SageMaker

## Project Overview
![ML WORKFLOW]([stepfunctions_graph.png](https://github.com/AmitRanjan235/ML-Workflow-For-Scones-Unlimited-On-Amazon-SageMaker/blob/2aa055f4404002515195cbe65ec3303f3faefc3f/stepfunctions_graph.png))

### Project Introduction
Image Classifiers are used in the field of computer vision to identify the content of an image and are applied across various industries. As a Machine Learning Engineer at Scones Unlimited, you will be working on an Image Classification model to enhance their scone delivery logistics.

### Background
Image classifiers are integral to computer vision and have applications in autonomous vehicles, augmented reality, eCommerce, and more. Your role at Scones Unlimited is to create an image classification model capable of identifying the type of vehicle delivery drivers use, optimizing routing and order assignments.

## Project Steps Overview
1. Data Staging
2. Model Training and Deployment
3. Lambdas and Step Function Workflow
4. Testing and Evaluation
5. Optional Challenge
6. Cleanup Cloud Resources

## Deploy and Monitor a Machine Learning Workflow for Image Classification

### Data Staging
We will use a sample dataset called CIFAR to simulate the challenges Scones Unlimited faces in image classification. To get started with CIFAR, we need to:

1. Extract the data from a hosting service.
2. Transform it into a usable shape and format.
3. Load it into a production system.

#### 1. Extract the data from the hosting service
In this section, we define a function `extract_cifar_data` that extracts the Python version of the CIFAR-100 dataset. The CIFAR dataset is open source and generously hosted by the University of Toronto at [https://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz](https://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz).

**Function definition:**
```python
import requests

def extract_cifar_data(url, filename="cifar.tar.gz"):
    # A function for extracting the CIFAR-100 dataset and storing it as a gzipped file

    # Arguments:
    # url      -- the URL where the dataset is hosted
    # filename -- the full path where the dataset will be written

    # Todo: request the data from the data URL
    # Hint: use `requests.get` method
    r = requests.get(url)
    with open(filename, "wb") as file_context:
        file_context.write(r.content)
    return
```
You can test this function by running the following cell and checking whether a new file named "cifar.tar.gz" is created in the file explorer:

```python

extract_cifar_data("https://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz")
```
#### 2. Transform the data into a usable shape and format
After extracting the data, we need to transform it into a format suitable for our machine learning workflow. In this section, we'll decompress the extracted dataset using the tarfile library:

```python

import tarfile

with tarfile.open("cifar.tar.gz", "r:gz") as tar:
    tar.extractall()
```
This will create a new folder named "cifar-100-python," which contains "meta," "test," and "train" files. These files are pickled and can be loaded using Python's pickle library:

```python

import pickle

with open("./cifar-100-python/meta", "rb") as f:
    dataset_meta = pickle.load(f, encoding='bytes')

with open("./cifar-100-python/test", "rb") as f:
    dataset_test = pickle.load(f, encoding='bytes')

with open("./cifar-100-python/train", "rb") as f:
    dataset_train = pickle.load(f, encoding='bytes')
```
The dataset_train and dataset_test objects contain information about the dataset, including filenames, labels, and the image data.

#### 3. Load the data
Now we can load the data into S3. Using the SageMaker SDK, grab the current region, execution role, and bucket:

```python

import sagemaker

sess = sagemaker.Session()

bucket = sess.default_bucket()
print("Default Bucket: {}".format(bucket))

region = sess.boto_region_name
print("AWS Region: {}".format(region))

role = sagemaker.get_execution_role()
print("RoleArn: {}".format(role))
```
With this data, we can easily sync your data up into S3:

```python

import os

os.environ["DEFAULT_S3_BUCKET"] = bucket
!aws s3 sync ./train s3://${DEFAULT_S3_BUCKET}/train/
!aws s3 sync ./test s3://${DEFAULT_S3_BUCKET}/test/
```


2. **Model Training and Deployment**

    - Generate metadata files for training.
    - Upload metadata files and image data to Amazon S3.
    - Create a SageMaker Estimator, set hyperparameters, and train the model.
    - Deploy the trained model as an endpoint.

3. **Lambdas and Step Function Workflow**

    - Author three Lambda functions for the workflow.
        1. The first Lambda returns an object to the Step Function as image_data in an event.
        2. The second Lambda is responsible for image classification.
        3. The third Lambda is responsible for filtering low-confidence inferences.
    - Compose the Lambdas together in a Step Function.
    - Export a JSON definition of the Step Function.
    - Provide a screenshot of the working Step Function.



4. **Testing and Evaluation**

    - Make predictions using a sample image.
    - Monitor the model for errors.

5. **Optional Challenge**

    - Explore additional challenges related to the project.

6. **Cleanup Cloud Resources**

    - Guidelines for cleaning up resources when done with the project.

## Success Criteria

### Model Training and Deployment

- Successfully completed the Model training section up to "Getting ready to deploy," demonstrating that the model was trained.
- Can construct an API endpoint associated with a model trained in SageMaker.
- Successfully completed the "Getting ready to deploy" section, showing that the trained ML model was deployed.
- Have a unique model endpoint name printed in the notebook for use later in the project.
- Successfully made predictions using a sample image.

### Build a Full Machine Learning Workflow

- Authored three Lambda functions.
    1. The first Lambda returns an object to the Step Function as image_data in an event.
    2. The second Lambda is responsible for image classification.
    3. The third Lambda is responsible for filtering low-confidence inferences.
- Saved the code for each Lambda function in a Python script.
- Can author a Step Function by composing Lambdas together.
- Have a JSON export that defines the Step Function.
- Provided a screenshot of the working Step Function.

### Monitor the Model for Errors

- Can extract Monitoring data from S3.
- Loaded the data from Model Monitor into the notebook.
- Can visualize Model Monitor data.
- Created custom visualizations of the Model Monitor data outputs.
