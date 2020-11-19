"""
This script is used for course notes.

Author: Erick Marin
Date: 10/12/2020
"""

# Recursion is the repeated application of the same procedure to a smaller
# problem.
# Recursion lets us tackle complex problems by reducing the problem to a
# a simpler one.  In programming, recursion is a way of doing a repetitive
# task by having a function call itself.


def factorial(n):   # Defining a function called factorial
    print("Factorial called with " + str(n))
    if n < 2:       # Conditional block defining the `base case`
        print("Returning 1")
        return 1
    # Function is call itself, 'recursive case`
    result = n * factorial(n - 1)
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result


factorial(4)

# The function sum_positive_numbers should return the sum of all positive
# numbers between the number n received and 1. For example, when n is 3 it
# should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15. Fill
# in the gaps to make this work:


def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return n

    # The recursive case is adding this number to
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n - 1)


print(sum_positive_numbers(3))  # Should be 6
print(sum_positive_numbers(5))  # Should be 15
