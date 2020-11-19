"""
This script is used for course notes.

Author: Erick Marin
Date: 10/11/2020
"""

# Infinite loop - a loop that keeps executing and never stops

# while x % 2 == 0:
#     x = x / 2

# To correct this inifinte loop

# if x != 0:
#     while x % 2 == 0:
#         x = x / 2

# or

# while x != 0 and x % 2 == 0:
#     x = x / 2


# The following code causes an infinite loop. Can you figure out what’s
# missing and how to fix it?
#
# def print_range(start, end):
#     # Loop through the numbers from start to end
#     n = start
#     while n <= end:
#         print(n)

def print_range(start, end):
    # Loop through the numbers from start to end
    n = start
    while n <= end:
        print(n)
        n += 1


print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line)

# Sometimes you actually want your program to execute continuously until some
# external condition is met.
#
# # Use the 'break' keyword to stop a loop from running
#
# # while True:
#   do_something_cool()
#   if user_requested_to_stop():
#       break
