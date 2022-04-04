import os
import cv2
import tarfile
import pydload
import logging
import numpy as np
import onnxruntime

# from .video_utils import get_interest_frames_from_video
# from .image_utils import load_images
from PIL import Image as pil_image

url = "https://github.com/notAI-tech/NudeNet/releases/download/v0/classifier_model.onnx"


home = os.getcwd() + "/"
model_folder = os.path.join(home, "models/")
if not os.path.exists(model_folder):
    os.mkdir(model_folder)

model_path = os.path.join(model_folder, os.path.basename(url))

if not os.path.exists(model_path):
    print("Downloading the checkpoint to", model_path)
    pydload.dload(url, save_to_path=model_path, max_time=None)


nsfw_model = onnxruntime.InferenceSession(model_path)