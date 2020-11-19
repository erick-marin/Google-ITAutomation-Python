"""
This script is used for course notes.

Author: Erick Marin
Date: 10/10/2020
"""

# while loop within a function

# Remember that the condition used by the while loop needs to evaluate to a
# condition of True or False


def attempts(n):
    x = 1   # Initializing variable
    while x <= n:
        print("Attempt " + str(x))
        x += 1  # Short-hand for x = x + 1
    print("Done")


attempts(5)
attempts(30)
