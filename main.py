import os

# import cv2
# import tarfile
# import pydload
# import logging
# import numpy as np
# import onnxruntime


from sexism._classifier import Classifier as NudeClassifier

data = "data/moovies/train/"

images = os.listdir(data)
images = [data + i for i in images]

classifier = NudeClassifier()

# Classify single image
classifier.classify(images[0])