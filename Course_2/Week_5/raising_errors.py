"""
This script is used for course notes.

Author: Erick Marin
Date: 12/26/2020
"""

from validations import validate_user

# print(validate_user("", -1))

print(validate_user("", 1))

print(validate_user("myuser", 1))

# This will generate an error because our code is trying to use the length
# function and we can't do that with integers.
# print(validate_user(88, 1))

print(validate_user([], 1))

# This will also produce an error
# print(validate_user(["name"], 1))

# This will produce an assertion error defined in the validations() function.
print(validate_user([3, 1]))

# Assertions will get removed from our code if we ask the interpreter to
# optimize it to run faster. So as a rule, we should use raise to check for
# conditions that we expect to happen during normal execution of our code and
# assert to verify situations that aren't expected but that might cause our
# code to misbehave.
