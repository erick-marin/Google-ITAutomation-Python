"""
This script is used for course notes.

Author: Erick Marin
Date: 12/19/2020
"""

import re

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)

# groups method returns a tuple of two elements of match groups created in the
# search.
print(result.groups())

# element at index 0
print(result[0])

print(result[1])
print(result[2])

print("{} {}".format(result[2], result[1]))


def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])


print(rearrange_name("Lovelace, Ada"))
print(rearrange_name("Ritchie, Dennis"))
print(rearrange_name("Hopper, Grace M."))


def rearrange_name_fixed(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])


print(rearrange_name_fixed("Kennedy, John F."))
print(rearrange_name_fixed("Hopper, Gracie M."))
