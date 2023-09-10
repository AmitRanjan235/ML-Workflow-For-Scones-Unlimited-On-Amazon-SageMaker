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

### Setting up this notebook
Notes about the instance size and kernel setup: This notebook has been tested on the Python 3 (Data Science) kernel and the ml.t3.medium SageMaker notebook instance.

### Data Staging

#### 1. Extract the data from the hosting service
We'll use a sample dataset called CIFAR to simulate the challenges faced by Scones Unlimited in image classification. To start working with CIFAR, we'll need to extract the data from the hosting service.

#### 2. Transform the data into a usable shape and format
After extracting the data, we'll transform it into a format suitable for our machine learning workflow. This involves decompressing the extracted dataset and preparing it for training and deployment.

Detailed instructions and code snippets are provided for each step in the project.

With this, you have completed the data staging process, preparing the CIFAR dataset for image classification. This dataset is now ready for training and deployment in Amazon SageMaker.
