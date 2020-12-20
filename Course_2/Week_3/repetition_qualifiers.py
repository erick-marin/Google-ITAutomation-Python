"""
This script is used for course notes.

Author: Erick Marin
Date: 12/19/2020
"""

import re

# Repeated matches
print(re.search(r"Py.*n", "Pygamlion"))

# Greedy repetitin qualifier
print(re.search(r"Py.*n", "Python Programming"))

# Zero results is also a possibility.  This search did not find
# any character from "a" to "z" mutiple times before "n".
print(re.search(r"Py[a-z]*n", "Pyn"))

# "+" reption qualifier searches how many occurences of "o" before an "l" and
# occurences of "l"
print(re.search(r"o+l+", "goldfish"))

print(re.search(r"o+l+", "woolly"))

# There is no match here because there was a character between the
# "o" and the "l".
print(re.search(r"o+l+", "boil"))

# The repeating_letter_a function checks if the text passed includes the
# letter "a" (lowercase or uppercase) at least twice.


def repeating_letter_a(text):
    result = re.search(r"[a|A].*[a|A]", text)
    return result is not None


print(repeating_letter_a("banana"))  # True
print(repeating_letter_a("pineapple"))  # False
print(repeating_letter_a("Animal Kingdom"))  # True
print(repeating_letter_a("A is for apple"))  # True

# The "?" repetion qualifier look for zero or one occurece of the character
# before it.
print(re.search(r"p?each", "To each their own"))

print(re.search(r"p?each", "I like peaches"))
