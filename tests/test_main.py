import pytest


data = "data/moovies/train/"


def test_import():

    from sexism import NudeClassifier


def test_init():

    from sexism import NudeClassifier

    classifier = NudeClassifier()


def test_predict():

    import os
    from sexism._classifier import Classifier as NudeClassifier

    images = os.listdir(data)
    images = [data + i for i in images]

    classifier = NudeClassifier()
    classifier.classify(images[0])