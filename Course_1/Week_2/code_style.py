"""
This script is used for course notes.

Author: Erick Marin
Date: 10/08/2020
"""


def calculate(d):
    """ No code style.  Difficult to understand wthat this function is
    for. """
    q = 3.14
    z = q * (d ** 2)
    print(z)


calculate(5)


def circle_area(radius):
    """ Code has been refactored.  This is easier understand what the
    function is for.  Calculate the area of a circle. """
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)


circle_area(5)

# This function to calculate the area of a rectangle is not very readable. Can
# you refactor it, and then call the function to calculate the area with base
# of 5 and height of 6? Tip: a function that calculates the area of a
# rectangle should probably be called rectangle_area, and if it's receiving
# base and height, that's what the parameters should be called.


def f1(x, y):
    z = x*y  # the area is base*height
    print("The area is " + str(z))


f1(5, 6)


def rectangle_area(base, height):
    """ Calculate the area of a rectangle using parameters `base`
    and `height` """

    area = base * height
    print("The area is " + str(area))


rectangle_area(5, 6)
