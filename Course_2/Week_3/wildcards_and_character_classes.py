"""
This script is used for course notes.

Author: Erick Marin
Date: 12/19/2020
"""

import re

print(re.search(r"[Pp]ython", "Python"))

print(re.search(r"[a-z]way", "The end of the highway"))

print(re.search(r"[a-z]way", "What a way to go"))

print(re.search("cloud[a-zA-z0-9]", "cloudy"))

print(re.search("cloud[a-zA-z0-9]", "cloud9"))


def check_punctuation(text):
    result = re.search(r"[,.:;?!]", text)
    return result != None


print(check_punctuation("This is a sentence that ends with a period."))  # True
print(check_punctuation("This is a sentence fragment without a period"))  # False
print(check_punctuation("Aren't regular expressions awesome?"))  # True
print(check_punctuation("Wow! We're really picking up some steam now!"))  # True
print(check_punctuation("End of the line"))  # False

# Searches any character from the beginning of sentence that is not included
# in the character classes.  It matches the first space character.
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))

# This character class group includes a space character.  It matches the
# the period "."
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

# "|" pipe symbol = either A or B
print(re.search(r"cat|dog", "I like cats."))
# This will only return the first result.
print(re.search(r"cat|dog", "I like both dogs and cats."))

# Use the findall() function to return all results.
print(re.findall(r"cat|dog", "I like both dogs and cats."))
