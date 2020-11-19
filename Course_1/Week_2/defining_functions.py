"""
This script is used for course notes.

Author: Erick Marin
Date: 10/08/2020
"""


def greeting(name, department):
    """ Print out a greeting with provided `name` and department
    parameters.  """

    print("Welcome, " + name)
    print("Your are part of " + department)

# Flesh out the body of the print_seconds function so that it prints the total
# amount of seconds given the hours, minutes, and seconds function parameters.
# Remember that there are 3600 seconds in an hour and 60 seconds in a minute.


def print_seconds(hours, minutes, seconds):
    """ Prints the total amount of seconds given the hours, minutes,
    and seconds function parameters. Note: There are 3600
    seconds in an hour and 60 seconds in a minute. """

    print((hours * 3600) + (minutes * 60) + seconds)


greeting("Blake", "IT Department")
print("\n")
greeting("Ellis", "Software Engineering")
print("\n")
print_seconds(1, 2, 3)
