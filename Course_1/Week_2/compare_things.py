"""
This script is used for course notes.

Author: Erick Marin
Date: 10/09/2020
"""

# True
print (10 > 1)

# False
print("cat" == "dog")

# True
print(1 != 2)

# This would result in an error because the computer knows that one is a
# number and the oter is a string.
# TypeError: '<' not supported between instances of 'int' and 'str'

# print(1 < "1")

# False
print(1 == "1")

# False
print("cat" == "Cat")

# False
print("cat" < "Cat")

# True
print("cat" > "Cat")

# Logical Operators

# To evaluate as true, the 'and' operatore would need both expressions to be
# true at at the same time.

# False
print("Yellow" > "Cyan" and "Brown" > "Magenta")

# True
print(25 > 60 or 1 != 2)

# True
print(not 42 == "Answer")
