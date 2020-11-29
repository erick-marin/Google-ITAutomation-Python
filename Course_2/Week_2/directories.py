"""
This script is used for course notes.

Author: Erick Marin
Date: 11/28/2020
"""

import os
# Use the "getcwd" method to get the current working directory.
print(os.getcwd())

# Use the "mkdir" function to create a new directory.
os.mkdir("new_dir")

# Use the "chdir" function to change working directory.
os.chdir("new_dir")
print(os.getcwd())
os.chdir("../")
print(os.getcwd())

# Use the "rmdir" function to remove directory.
os.mkdir(
    "/home/k/Documents/Devs/Google-ITAutomation-Python/Course_2/Week_2/"
    "newer_dir")
os.rmdir(
    "/home/k/Documents/Devs/Google-ITAutomation-Python/Course_2/Week_2/"
    "newer_dir")

# To remove directories the must be empty. To view if there a files in a
# directory you can use the "os.listdir" function.
print(os.listdir(
    "/home/k/Documents/Devs/Google-ITAutomation-Python/Course_2/Week_2"))

# To find out what they are, we can use functions like "os.path.isdir" but
# before we look at how that works. See how the list contains just file
# names. If we want to know whether one of these files is a directory,
# we need to use os.path.join to create the full path.
dir = "/home/k/Documents/Devs/Google-ITAutomation-Python/Course_2/Week_2/"
for name in os.listdir(dir):
    # Creates a string containing cross-platform concatenated directories. By
    # using os.path.join we can concatenate directories in a way that can be
    # used with other os.path() functions.
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))
