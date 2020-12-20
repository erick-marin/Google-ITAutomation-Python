"""
This script is used for course notes.

Author: Erick Marin
Date: 12/20/2020
"""

import re

# split() function
result = re.split(r"[.?!]", "One sentence. Another one? And the last one!")
print(result)
# Adding a capturing group will result in giving us the elements used in the
# character class to split the values.
result = re.split(r"([.?!])", "One sentence. Another one? And the last one!")
print(result)

# sub() function to replace string with an expression that was matched.
result = re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]",
                "Recieved an email for go_nuts95@my.example.com")
print(result)

# Use parentheses to create capturing groups. In the first parameter, we've got
# an expression that contains the two groups that we want to match: one before
# the comma and one after the comma. We want to use a second parameter to
# replace the matching string. We use backslash two to indicate the second
# captured group followed by a space and backslash one to indicate the first
# captured group. When referring to captured groups, a backslash followed by a
# number indicates the corresponding captured group.
result = re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")
print(result)


result = re.split(r"the|a", "One sentence. Another one? And the last one!")
print(result)
