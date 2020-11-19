"""
This script is used for course notes.

Author: Erick Marin
Date: 10/10/2020
"""

# `for` loop - Iterates over a sequence of values

for x in range(5):  # List of numbers generated will be one less than the
    print(x)        # given value

# - In Python, a range of numbers wills start with the value 0 by default

# Fill in the gaps of the sum_squares function, so that it returns the sum of
# all the squares of numbers between 0 and x (not included). Remember that you
#  can use the range(x) function to generate a sequence of numbers from 0 to x
# (not included).


def square(n):
    return n*n


def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum


print(sum_squares(10))  # Should be 285

friends = ["Taylor", "Alex", "Pat", "Eli"]  # List created with square brackets
for friend in friends:
    print("Hi " + friend)


values = [23, 52, 59, 37, 48]
SUM = 0
LENGTH = 0
for value in values:
    SUM += value
    LENGTH += 1

print("Total sum: " + str(SUM) + " - Average: " + str(SUM/LENGTH))

# Use `for` loops when there's a sequence of elements that you want to iterate.
# Use 'while' loops when you want to repeat an action until a condition
# changes.
