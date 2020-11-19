"""
This script is used for course notes.

Author: Erick Marin
Date: 10/07/2020
"""

print("a" + "b" + "c")

print("This " + "is "+ "pretty " + "neat!")

BASE = 6
HEIGHT = 3
AREA = (BASE * HEIGHT) / 2
print("The area of the triangle is: " + str(AREA))

# In this scenario, we have a directory with 5 files in it. Each file has a
# different size: 2048, 4357, 97658, 125, and 8. Fill in the blanks to
# calculate the average file size by having Python add all the values for you,
# and then set the files variable to the number of files. Finally, output a
# message saying "The average size is: " followed by the resulting number.
# Remember to use the str() function to convert the number into a string.

TOTAL = 2048 + 4357 + 97658 + 125 + 8
FILES = 5
AVERAGE = TOTAL / FILES
print("The average size is: " + str(AVERAGE))
