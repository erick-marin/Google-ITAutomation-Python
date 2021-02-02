#!/usr/bin/env python3

import os
import requests

# List all .txt files under /data/feedback directory that contains the actual
# feedback to be displayed on the company's website.
dir_path = "/data/feedback/"
folder = os.listdir(dir_path)

# Have a list that contains all of the feedback files from the path
list = []

for feedback in folder:
    with open(dir_path + feedback, "r") as file:
        # Create a list from dictionary keys and values by using title, name,
        # date, and feedback as keys for the content value
        list.append({"title": file.readline().rstrip("\n"),
                     "name": file.readline().rstrip("\n"),
                     "date": file.readline().rstrip("\n"),
                     "feedback": file.read().rstrip("\n")})

for item in list:
    resp = requests.post("http://35.188.47.100/feedback/", json=item)
    if resp.status_code != 201:
        raise Exception(
            "Post failed with error status code {}".format(resp.status_code))
    print("Added feedback ID: {}".format(resp.json()["id"]))
