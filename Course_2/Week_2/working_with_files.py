"""
This script is used for course notes.

Author: Erick Marin
Date: 11/28/2020
"""

import os
# Remove a file
# os.remove("Course_2/Week_2/novel.txt")

# Rename a file
# os.rename("Course_2/Week_2/First_Draft.txt",
#           "Course_2/Week_2/Finished_Masterpiece.txt")

# Check whether a file exists
status = os.path.exists("Course_2/Week_2/Finished_Masterpiece.txt")
print(status)  # True because it exists.

status = os.path.exists("Course_2/Week_2/First_Draft.txt")
print(status)  # False because it does not exist.
