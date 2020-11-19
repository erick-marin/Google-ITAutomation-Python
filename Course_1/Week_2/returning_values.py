"""
This script is used for course notes.

Author: Erick Marin
Date: 10/08/2020
"""


def area_triangle(base, height):
    """ Calculate the area of triange by multipling `base` by `height` """

    return base * height / 2


def get_seconds(hours, minutes, seconds):
    """ Calculate the `hours` and `minutes` into seconds, then add with
    the `seconds` paramater. """

    return 3600*hours + 60*minutes + seconds


def convert_seconds(seconds):
    """ Convert the duration of time in 'seconds' to the equivalent
    number of hours, minutes, and seconds.  """

    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


def greeting(name):
    """ Print out a greeting with provided `name` parameter.  """

    print("Welcome, " + name)


AREA_A = area_triangle(5, 4)
AREA_B = area_triangle(7, 3)
SUM = AREA_A + AREA_B
print("The sum of both areas is: " + str(SUM))

AMOUNT_A = get_seconds(2, 30, 0)
AMOUNT_B = get_seconds(0, 45, 15)
result = AMOUNT_A + AMOUNT_B
print(result)

HOURS, MINUTES, SECONDS = convert_seconds(5000)
print(HOURS, MINUTES, SECONDS)

# Assigning result of a function call, where the function has no return
# will result in 'None'
RESULT = greeting("Christine")
print(RESULT)
