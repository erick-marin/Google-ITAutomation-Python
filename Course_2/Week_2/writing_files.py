"""
This script is used for course notes.

Author: Erick Marin
Date: 11/28/2020
"""

# With block pattern we open a file called "novel.txt". Using the write method
# on a file object writes contents to it instead of reading from it. By
# default, the "open" function uses the "r" mode, which stands for read only.
# The second argument to the open method governs what you can do with the file
# you've just opened. The w character tells the open function that we want to
# open the file for writing only. If the file doesn't exist then Python will
# create it.
with open("Course_2/Week_2/novel.txt", "w") as file:
    file.write("It was a dark and stormy night")
