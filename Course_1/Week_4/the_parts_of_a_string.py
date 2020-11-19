"""
This script is used for course notes.

Author: Erick Marin
Date: 10/11/2020
"""

# String indexing
name = "Jaylen"

print(name[1])

# Python starts counting indices from 0 and not 1

print(name[0])

# The last index of a string will always be the one less than the length of
# the string.

print(name[5])

# If we try to access index past the characters availble, we get an index
# error telling us that it's out of range.

# print(name[6])
# IndexError: string index out of range

# Using negative indexes lets us access the positions in the string starting
# from the last.

""" text = "Random string with a lot of characters"
print(text[-1])
print(text[-2]) """

# Want to give it a go yourself? Be my guest! Modify the first_and_last
# function so that it returns True if the first letter of the string is the
# same as the last letter of the string, False if they’re different. Remember
# that you can access characters using message[0] or message[-1]. Be careful
# how you handle the empty string, which should return True since nothing is
# equal to nothing.


def first_and_last(message):
    emptystr = ""
    if message == emptystr:
        return True
    elif message[0] == message[-1]:
        return True
    return False


print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

# Slice - The portion of a string that can contain more than one character;
# also sometimes called a substring.

color = "Orange"
# In this case, we start with indexed one, the second letter of the string,
# and go up to index three, the fourth letter of the string.
print(color[1:4])

fruit = "Pineapple"
print(fruit[:4])

print(fruit[4:])
