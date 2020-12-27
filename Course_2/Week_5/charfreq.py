#!/usr/bing/env python3

"""
This script is used for course notes.

Author: Erick Marin
Date: 12/26/2020
"""


# To use a try-except block, we need to be aware of the errors that functions
# that we're calling might raise. This information is usually part of the
# documentation of the functions. Once we know this we can put the operations
# that might raise errors as part of the try block, and the actions to take
# when errors are raised as part of a corresponding except block.

def character_frequency(filename):
    """Count the frequency of a character in a given file."""
    # First try to open the file
    try:
        f = open(filename)
    except OSError:
        return None

    # now process the file
    characters = {}
    for line in f:
        for char in line:
            characters[char] = characters.get(char, 0) + 1
    f.close()
    return characters
