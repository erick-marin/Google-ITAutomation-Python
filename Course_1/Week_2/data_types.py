"""
This script is used for course notes.

Author: Erick Marin
Date: 10/07/2020
"""

# Generally, your computer doesn't know how to mix different data types. For
# example, adding two integers together makes perfect sense to computers>

print("\n")
print(7 + 8)
print("\n")

# Adding together two strings also makes sense. We just end up with the longer
# strings that contains the two.

print("Hello " + "World\n")

# But your computer doesn't know how to add an integer and a string. If you
# tell it to mix these two different data types, your computer isn't going to
# know what to do and will raise an error.

# print(7 + "8")

# Traceback (most recent call last):
#   File "/home/k/Documents/Devs/GoogleITAutomation-Python/Week 2/
#       datatypes.py", line 23, in <module>
#     print(7 + "8")
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Think about data types in terms of information they can represent. If you're
# ever not sure what data types a certain value is, Python gives you a handy
# way to find out. You can use the type function, to have the computer tell
# you the type. This might come in handy when dealing with code that someone
# else wrote and you're not sure what data types it's using.

print(type("a"))
print(type(2))
print(type(2.5))
