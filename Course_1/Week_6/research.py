"""
This script is used for course notes.

Author: Erick Marin
Date: 10/11/2020
"""

# `sort` method
# The method modified returns the same list reorganized.
numbers = [4, 6, 2, 7, 1]
numbers.sort()
print(numbers)

# `sorted` function
# The function returns  a new sorted list but the original list is still the
# same.
names = ["Carlos", "Ray", "Alex", "Kelly"]
print(names)
print(sorted(names))

# Default approach for sorting list is alphabetically.
# But you can sort by other methods, like based on the return value of a
# function.
print(sorted(names, key=len))
