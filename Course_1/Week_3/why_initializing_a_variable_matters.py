"""
This script is used for course notes.

Author: Erick Marin
Date: 10/10/2020
"""

# If you do not initialize a variable

# while my_variable < 10:
#     print("Hello")
#     my_variable += 1

# You will recieve the following error:

# Traceback (most recent call last):
# File "/home/k/Documents/Devs/...<module>
#    while my_variable < 10:
# NameError: name 'my_variable' is not defined

# This is 'NameError' type

# This easy to correct:

my_variable = 5

while my_variable < 10:
    print("Hello")
    my_variable += 1

#  If we reuse the variable without setting the correct value from the start,
#  it will still have the value from before.
#
#  The first while loop is correct

x = 1
sum = 0
while x < 10:
    sum += x
    x += 1

# This second while loop is incorrect.
# We're initializing product but forgetting to initialize x. So x is still 10,
# this means that when the while condition gets checked, x is already 10 at
# the start of the iteration. The while condition is false before it even
# starts and the body never executes.

product = 1
while x < 10:
    product = product * x
    x += 1

print(sum, product)

# You will need to initialize 'x' again to 0 to correct.

# Here ia another example of a while loop within a function.


def count_down(start_number):
    current = start_number
    while current > 0:
        print(current)
        current -= 1
    print("Zero!")

count_down(3)
