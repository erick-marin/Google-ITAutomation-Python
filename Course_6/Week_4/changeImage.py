#!/usr/bin/env python3

import os
from PIL import Image

dir_path = os.path.expanduser("~") + "/supplier-data/images/"

"""
The raw images from images subdirectory contains alpha transparency layers.
So, it is better to first convert RGBA 4-channel format to RGB 3-channel
format before processing the images. Use convert("RGB") method for converting
RGBA to RGB image.
"""

for image in os.listdir(dir_path):
    if ".tiff" in image and "." not in image[0]:
        img = Image.open(dir_path + image).convert("RGB")
        # Change image resolution from 3000x2000 to 600x400 pixel.
        # After processing the images, save them in the same path
        # ~/supplier-data/images, with a JPEG extension.
        img.resize((600, 400)).save(
            dir_path + image.split(".")[0] + ".jpeg", "jpeg")
        img.close()
