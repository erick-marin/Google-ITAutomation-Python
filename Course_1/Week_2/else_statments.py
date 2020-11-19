"""
This script is used for course notes.

Author: Erick Marin
Date: 10/09/2020
"""


def hint_username(username):
    """ If username is less than than 3 characters, print message else
    , if valid length, print message.  """
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        print("Valid username")


hint_username("Al")
hint_username("Delcy")

# When a return statement is executed when the if statement is True, the
# function exits so that the code that follows doesn't get executed.  In other
# words, anything that comes after that will only be executed if the condition
# in the if statement was false.


def is_positive(number):
    """ The is_positive function should return True if the number
    received is positive and False if it isn't. """
    if number > 0:
        return True
    else:
        return False


print(is_positive(-5))
print(is_positive(0))
print(is_positive(13))

# Remember that this technique can only be used when you're returning a value
# inside the if statement.

def is_even(number):
    """ If number is divisible by 2 with a remainder equal to 0, then
    return True, if not then return False. """
    if number % 2 == 0:
        return True
    return False


print(is_even(4))   # True
print(is_even(11))  # False
print(is_even(3))   # False
