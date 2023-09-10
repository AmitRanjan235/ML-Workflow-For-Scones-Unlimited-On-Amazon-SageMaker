<!DOCTYPE html>
<html>
<head>
    <title>Deploy and Monitor a Machine Learning Workflow for Image Classification</title>
</head>
<body>
    <h1>Setting up this notebook</h1>
    <p><strong>Notes about the instance size and kernel setup:</strong> This notebook has been tested on</p>
    <ul>
        <li>The Python 3 (Data Science) kernel.</li>
        <li>The ml.t3.medium SageMaker notebook instance.</li>
    </ul>

    <h2>Data Staging</h2>
    <p>We will use a sample dataset called CIFAR to simulate the challenges Scones Unlimited faces in image classification. To get started with CIFAR, we need to:</p>
    <ol>
        <li>Extract the data from a hosting service.</li>
        <li>Transform it into a usable shape and format.</li>
        <li>Load it into a production system.</li>
    </ol>

    <h3>1. Extract the data from the hosting service</h3>
    <p>In this section, we define a function <code>extract_cifar_data</code> that extracts the Python version of the CIFAR-100 dataset. The CIFAR dataset is open source and generously hosted by the University of Toronto at <a href="https://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz">https://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz</a>.</p>
    
    <p><em>Function definition:</em></p>
    <pre><code>import requests

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
    return</code></pre>

    <p>You can test this function by running the following cell and checking whether a new file named "cifar.tar.gz" is created in the file explorer:</p>
    <pre><code>extract_cifar_data("https://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz")</code></pre>

    <h3>2. Transform the data into a usable shape and format</h3>
    <p>After extracting the data, we need to transform it into a format suitable for our machine learning workflow. In this section, we'll decompress the extracted dataset using the <code>tarfile</code> library:</p>
    <pre><code>import tarfile

with tarfile.open("cifar.tar.gz", "r:gz") as tar:
    tar.extractall()</code></pre>

    <p>This will create a new folder named "cifar-100-python," which contains "meta," "test," and "train" files. These files are pickled and can be loaded using Python's <code>pickle</code> library:</p>
    <pre><code>import pickle

with open("./cifar-100-python/meta", "rb") as f:
    dataset_meta = pickle.load(f, encoding='bytes')

with open("./cifar-100-python/test", "rb") as f:
    dataset_test = pickle.load(f, encoding='bytes')

with open("./cifar-100-python/train", "rb") as f:
    dataset_train = pickle.load(f, encoding='bytes')</code></pre>

    <p>The <code>dataset_train</code> and <code>dataset_test</code> objects contain information about the dataset, including filenames, labels, and the image data.</p>

    <!-- Other code snippets removed for brevity -->

    <p>With this, you have completed the data staging process, extracting, transforming, and loading the CIFAR dataset for image classification. This prepared dataset can now be used for training and deploying your image classification model in Amazon SageMaker.</p>
</body>
</html>
