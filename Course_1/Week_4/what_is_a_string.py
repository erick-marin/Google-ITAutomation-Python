"""
This script is used for course notes.

Author: Erick Marin
Date: 10/11/2020
"""

# A string is a data type in Python that's used to represent a piece of text.
# It's written between quotes, either double quotes or single quotes, your
# choice.

name = "Sasha"
color = 'gold'

# If you mix match double and singl quotes you will recieve a 'SynataxError'
# place = "Cambridge'

# SyntaxError: EOL while scanning string literal

# Empty string
pet = ""
pet = "looooooooooooooooooooooooooooong cat"

#  Concatenation
print("Name: " + name + ", Favorite color: " + color)

print("example" * 3)

# `1en` function tells the number of funtions contained in a string
print(len(pet))

# Modify the double_word function so that it returns the same word repeated
# twice, followed by the length of the new doubled word. For example,
# double_word("hello") should return hellohello10.


def double_word(word):
    return word * 2 + str(len(word*2))


print(double_word("hello"))  # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0
