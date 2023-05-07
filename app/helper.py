# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/helper.ipynb (unless otherwise specified).

__all__ = ['perform_ocr', 'find_img']

# Cell
import io
import os
import re
import random
from datetime import datetime
from google.cloud import vision

# Cell
def perform_ocr(client, image_file):
    with io.BytesIO(image_file) as image_bin:
        content = image_bin.read()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    return texts

def find_img(rand_dir: str, spec_img_path=None)-> str:
    """
    Getting an image randomly or by specific path.

    Args:
        directory (str): directory
        specific_image_path (_type_, optional): _description_. Defaults to None.

    Returns:
        str: _description_
    """
    if spec_img_path:
        return spec_img_path
    # Search for all .jpg files in the specified directory and its subdirectories
    image_files = []
    for root, dirs, files in os.walk(rand_dir):
        for file in files:
            if file.lower().endswith('.jpg'):
                image_files.append(os.path.join(root, file))

    # If there are no image files, return None
    if not image_files:
        return None

    # Pick a random image file from the list of image files found, and return its path
    random_image_path = random.choice(image_files)
    return random_image_path