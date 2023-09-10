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
You can test this function by running the following cell and checking whether a new file named "cifar.tar.gz" is created in the file explorer:

python
Copy code
extract_cifar_data("https://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz")
2. Transform the data into a usable shape and format
After extracting the data, we need to transform it into a format suitable for our machine learning workflow. In this section, we'll decompress the extracted dataset using the tarfile library:

python
Copy code
import tarfile

with tarfile.open("cifar.tar.gz", "r:gz") as tar:
    tar.extractall()
This will create a new folder named "cifar-100-python," which contains "meta," "test," and "train" files. These files are pickled and can be loaded using Python's pickle library:

python
Copy code
import pickle

with open("./cifar-100-python/meta", "rb") as f:
    dataset_meta = pickle.load(f, encoding='bytes')

with open("./cifar-100-python/test", "rb") as f:
    dataset_test = pickle.load(f, encoding='bytes')

with open("./cifar-100-python/train", "rb") as f:
    dataset_train = pickle.load(f, encoding='bytes')
The dataset_train and dataset_test objects contain information about the dataset, including filenames, labels, and the image data.
