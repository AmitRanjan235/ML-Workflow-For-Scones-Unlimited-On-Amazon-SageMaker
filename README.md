<!DOCTYPE html>
<html>
<head>
    <title>Deploy and Monitor a Machine Learning Workflow for Image Classification</title>
</head>
<body>
    <h1>Deploy and Monitor a Machine Learning Workflow for Image Classification</h1>

    <h2>Setting up this notebook</h2>
    <p>Notes about the instance size and kernel setup:</p>
    <p>This notebook has been tested on:</p>
    <ul>
        <li>The Python 3 (Data Science) kernel</li>
        <li>The ml.t3.medium SageMaker notebook instance</li>
    </ul>

    <h2>Data Staging</h2>

    <h3>1. Extract the data from the hosting service</h3>
    <p>
        In the following cell, we define a function <code>extract_cifar_data</code> that extracts the Python version of the CIFAR-100 dataset.
        The CIFAR dataset is open source and generously hosted by the University of Toronto at
        <a href="https://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz">https://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz</a>.
    </p>
    <!-- Code snippet omitted -->

    <h3>2. Transform the data into a usable shape and format</h3>
    <p>
        After extracting the data, we need to transform it into a format suitable for our machine learning workflow.
        In this section, we'll decompress the extracted dataset using the <code>tarfile</code> library.
    </p>
    <!-- Code snippet omitted -->

    <p>
        Now that you have completed the data staging process, extracting, transforming, and loading the CIFAR dataset for image classification.
        This prepared dataset can now be used for training and deploying your image classification model in Amazon SageMaker.
    </p>
</body>
</html>
