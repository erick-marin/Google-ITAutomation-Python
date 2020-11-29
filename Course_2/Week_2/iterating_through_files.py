"""
This script is used for course notes.

Author: Erick Marin
Date: 11/28/2020
"""

with open("Course_2/Week_2/spider.txt") as file:
    for line in file:
        print(line.upper())

# when Python reads the file line by line, the line variable will always have
# a new line character at the end. In other words, the newline character is
# not removed when calling read line. When we ask Python to print the line,
# the print function adds another new line character, creating an empty line.
# We can use a string method, strip to remove all surrounding white space,
# including tabs and new lines.

with open("Course_2/Week_2/spider.txt") as file:
    for line in file:
        print(line.strip().upper())

# Another way we can work with the contents of the file is to read the file
# lines into a list. Then, we can do something with the lists like sort
# contents.

file = open("Course_2/Week_2/spider.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)
