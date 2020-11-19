"""
This script is used for course notes.

Author: Erick Marin
Date: 10/09/2020
"""


def hint_username(username):
    """ If username is less than than 3 characters, print message
    elseif username is greatn than 15 characters, print message
    else if valid length, print message.  """
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long")
    else:
        print("Valid username")


hint_username("Al")
hint_username("Administrator009")
hint_username("Delcy")


def number_group(number):
    """ The number_group function should return "Positive" if the
    number received is positive, "Negative" if it's negative, and
    "Zero" if it's 0. """

    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


print(number_group(10))  # Should be Positive
print(number_group(0))  # Should be Zero
print(number_group(-5))  # Should be Negative
