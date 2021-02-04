#! /usr/bin/env python3

import os
import requests

supplier_desc_path = os.path.expanduser("~") + "/supplier-data/descriptions/"
supplier_image_path = os.path.expanduser("~") + "/supplier-data/images/"

text_files = sorted(os.listdir(supplier_desc_path))
image_files = sorted([image_name for image_name in os.listdir(
    supplier_image_path) if ".jpeg" in image_name])

list = []

for text_file in text_files:
    with open(supplier_desc_path + text_file, "r") as f:
        data = {"name": f.readline().rstrip("\n"),
                "weight": int(f.readline().rstrip("\n").split(" ")[0]),
                "description": f.readline().rstrip("\n")}

        for image_file in image_files:
            if image_file.split(".")[0] in text_file.split(".")[0]:
                data["image_name"] = image_file

        list.append(data)

for item in list:
    resp = requests.post("http://127.0.0.1:80/fruits/", json=item)
    if resp.status_code != 201:
        raise Exception("Post error status={}".format(resp.status_code))
    print("Created feedback ID: {}".format(resp.json()["id"]))
