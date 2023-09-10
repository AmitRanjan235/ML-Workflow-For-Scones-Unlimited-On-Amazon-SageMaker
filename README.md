# Project: Build a ML Workflow For Scones Unlimited On Amazon SageMaker

## Project Overview

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
