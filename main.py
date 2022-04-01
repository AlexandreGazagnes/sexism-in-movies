import os
from nudenet import NudeClassifier


# data = "data/moovies/train"

# images = os.listdir(data)
# images = [data+i for i in images]

classifier = NudeClassifier()

# Classify single image
classifier.classify("path_to_image_1")
