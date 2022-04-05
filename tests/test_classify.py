import os
import pytest

from sexism import NudeClassifier


# bikini = "data/images/bikini_not_bikini/bikini/"
# not_bikini = "data/images/bikini_not_bikini/not_bikini/"


def classify_one():

    bikini = "data/images/bikini_not_bikini/bikini/"

    images = os.listdir(bikini)
    bikini = [bikini + i for i in images]

    classifier = NudeClassifier()
    classifier.classify(bikini[0])


def test_classify_bikini():

    bikini = "data/images/bikini_not_bikini/bikini/"

    images = os.listdir(bikini)
    bikini = [bikini + i for i in images]

    classifier = NudeClassifier()
    preds = classifier.classify(bikini)

    # compute rate
    bikini_rate = sum([i["unsafe"] for i in preds.values()]) / len(images)

    assert bikini_rate > 0.7


def test_classify_not_bikini():

    not_bikini = "data/images/bikini_not_bikini/not_bikini/"

    images = os.listdir(not_bikini)
    bikini = [not_bikini + i for i in images]

    classifier = NudeClassifier()
    preds = classifier.classify(bikini)

    # compute rate
    bikini_rate = sum([i["unsafe"] for i in preds.values()]) / len(images)

    assert bikini_rate < 0.2