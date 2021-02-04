#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"
image_dir = os.path.expanduser("~") + "/supplier-data/images/"
jpeg_images = [image for image in os.listdir(image_dir) if ".jpeg" in image]

for image in jpeg_images:
    with open(image_dir + image, "rb") as opened:
        r = requests.post(url, files={"file": opened})
