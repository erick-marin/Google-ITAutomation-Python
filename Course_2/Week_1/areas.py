"""
This script is used for course notes.

Author: Erick Marin
Date: 10/28/2020
"""

import math


def triangle(base, height):
    """Calculate the area of a triangle."""
    return base * height / 2


def rectangle(base, height):
    """Calculate the area of a rectangle."""
    return base * height


def circle(radius):
    """Calculate the area of a circle."""
    return math.pi * (radius ** 2)


def donut(outside_radius, inside_radius):
    """Calculate the radius of a donut."""
    return circle(outside_radius) - circle(inside_radius)
