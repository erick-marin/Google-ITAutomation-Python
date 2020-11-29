"""
This script is used for course notes.

Author: Erick Marin
Date: 11/28/2020
"""

from datetime import date
import os
import datetime
# Check how big a file is with getsize() function in bytes.
fileSize = os.path.getsize(
    "Course_2/Week_2/spider.txt")
print(fileSize)

# Check when a file was modified with getmtime() function. Returns a Unix
# timestamp. It represents the number of seconds since January 1st, 1970.
# That's when they started publishing Unix operating systems, Unix uses that
# date because there couldn't be any file created before that time.
modifiedTime = os.path.getmtime("Course_2/Week_2/spider.txt")
print(modifiedTime)  # Unix timestamp

# Using "fromtimestamp" method from "datetime" class from imported "datetime"
# module.
print(datetime.datetime.fromtimestamp(modifiedTime))

# The "abspath" function constructs the full path of the file in the current
# working directory.
filePath = os.path.abspath("spider.txt")
print(filePath)
