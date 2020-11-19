"""
This script is used for course notes.

Author: Erick Marin
Date: 10/08/2020
"""

NAME = "Kay"
NUMBER = len(NAME) * 9

print("Hello " + NAME + ". Your lucky number is " + str(NUMBER))

NAME = "Cameron"
NUMBER = len(NAME) * 9

print("Hello " + NAME + ". Your lucky number is " + str(NUMBER))


def lucky_number(name):
    """ Calculate the lucky number by using string length of 'name'
    parameter """

    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))


lucky_number("Kay")
lucky_number("Cameron")


# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
# june_days = 30
# print("June has " + str(june_days) + " days.")
# july_days = 31
# print("July has " + str(july_days) + " days.")


def month_days(month, days):
    """ Print out the month and days. """

    print(month + " has " + str(days) + " days.")


month_days("June", 30)
month_days("July", 31)
