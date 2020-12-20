"""
This script is used for course notes.

Author: Erick Marin
Date: 12/20/2020
"""

import re

# numeric repetion qualifiers created with curly brackets
# match a string with 5 consecutive letters using the defined character class.
print(re.search(r"[a-zA-Z]{5}", "a ghost"))

# Use the "find all" method to return all the matches
# This result identfied "appea" becuase it has more than 5 consecutive letters.
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))

# Use "\b" with matches word limits indicating we want full words for the
# pattern search. This will return on full words with 5 characters.
print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared"))

# Use ranges as well with the repetition qualifier
# This returns a string with 5 to 10 consecutive characters
print(re.findall(r"\w{5,10}", "I really like strawberries"))
# This retuns a string with 5 or more consecutive characters
print(re.findall(r"\w{5,}", "I really like strawberries"))
# This returns a string that starts with "s" followed by 0 to 20 consecutive
# alphanumeric characters including underscores.
print(re.findall(r"s\w{,20}", "I really like strawberries"))

# The long_words function returns all words that are at least 7 characters.
# Fill in the regular expression to complete this function.


def long_words(text):
    pattern = r"\b\w{7,}\b"
    result = re.findall(pattern, text)
    return result


print(long_words("I like to drink coffee in the morning."))  # ['morning']
# ['chocolate', 'afternoon']
print(long_words("I also have a taste for hot chocolate in the afternoon."))
print(long_words("I never drink tea late at night."))  # []
