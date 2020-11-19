"""
This script is used for course notes.

Author: Erick Marin
Date: 10/12/2020
"""

# Folders that contain folders that contain folders are an example
# of recursive structures that can take advantage of a recursive
# function.

# In Python you can call a recursion function by default 1000 times.
# Recursion might work well for a directory structure but not for
# mathematics.

# Recommended to using recursion only when you need to go through a recursive
# structure that won't reach a thousand nested levels.


def factorial(n):   # Defining a function called factorial
    print("Factorial called with " + str(n))
    if n < 2:       # Conditional block defining the `base case`
        print("Returning 1")
        return 1
    # Function is call itself, 'recursive case`
    result = n * factorial(n - 1)
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result


factorial(1000)

# You'll get an error:
# RecursionError: maximum recursion depth exceeded while calling a Python
# object
