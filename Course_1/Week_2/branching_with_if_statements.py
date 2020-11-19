"""
This script is used for course notes.

Author: Erick Marin
Date: 10/09/2020
"""


def hint_username(username):
    """ If username is less than than 3 characters, print message  """
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")


hint_username("I")


def is_positive(number):
    """ The is_positive function should return "True" if the number
    received is positive, otherwise it returns "None".  """
    if number > 0:
        return True
    return None


print(is_positive(-5))
print(is_positive(0))
print(is_positive(13))
