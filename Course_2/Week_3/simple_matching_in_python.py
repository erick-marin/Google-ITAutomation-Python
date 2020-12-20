"""
This script is used for course notes.

Author: Erick Marin
Date: 12/19/2020
"""

import re

result = re.search(r"aza", "plaza")
print(result)

result = re.search(r"aza", "bazaar")
print(result)

result = re.search(r"aza", "maze")
print(result)

print(re.search(r"^x", "xenon"))

print(re.search(r"p.ng", "clapping"))

print(re.search(r"p.ng", "sponge"))


def check_aei(text):
    result = re.search(r".a.e.i.", text)
    return result is not None


print(check_aei("academia"))  # True
print(check_aei("aerial"))  # False
print(check_aei("paramedic"))  # True

print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))
