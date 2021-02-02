#!/usr/bin/env python3

"""
Convert images to proper format.

Iterate through each image to rotate, resize, and save image in a diffrent
format.

Author: Erick Marin
Date: 01/29/2021
"""

from PIL import Image
import os

# Original source folder with images
source_dir = os.path.expanduser("~") + "/images/"
# Destination folder for converted images
destination_dir = "/opt/icons/"

# Iterate through each file in the folder
for image in os.listdir(source_dir):
    if "." not in image[0]:
        new_image = Image.open(source_dir + image)
        # Rotate the image 90° clockwise, resize the image from 192x192 to
        # 128x128, convert image to RGB profile, then save to new directory
        # /opt/icons/ renamed with "jpeg" extension.
        new_image.rotate(270).resize((128, 128)).convert("RGB").save(
            destination_dir + image.split(".")[0], "jpeg")
        new_image.close()
