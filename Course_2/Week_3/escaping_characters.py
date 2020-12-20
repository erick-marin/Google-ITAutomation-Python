"""
This script is used for course notes.

Author: Erick Marin
Date: 12/19/2020
"""

import re

# If we wanted to search for an actual "period" in string we have to escape
# the character.  The example below would not work to find literal ".com".
print(re.search(r".com", "welcome"))

# We need to use the "\" backslash escape character.
print(re.search(r"\.com", "welcome"))

print(re.search(r".com", "mydomain.com"))

# "\w" matches any alphanumeric character; letters, number and underscores
print(re.search(r"\w*", "This is an example"))

print(re.search(r"\w*", "And_this_is_another"))


# The function checks if the text passed has at least 2 groups of alphanumeric
# characters (including letters, numbers, and underscores) separated by one or
# more whitespace characters.
def check_character_groups(text):
    result = re.search(r"\w*\s+\w*$", text)
    return result is not None


print(check_character_groups("One"))  # False
print(check_character_groups("123  Ready Set GO"))  # True
print(check_character_groups("username user_01"))  # True
print(check_character_groups("shopping_list: milk, bread, eggs."))  # False
