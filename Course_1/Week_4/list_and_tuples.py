"""
This script is used for course notes.

Author: Erick Marin
Date: 10/19/2020
"""

# Tuples are written with parenthesis. We use tuples when we want to make sure an element
# in a certain position or index refers to one specific thing and won't change.
fullname = ("Grace", "M", "Hopper")


def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

# When a function is returning more than one values, it's actually returning a
# tuple.


result = convert_seconds(5000)
print(type(result))
print(result)

# You can unpack the tuple
hours, minutes, seconds = result
print(hours, minutes, seconds)

# We can also do this directly when calling the function without the
# intermediate result variable.

hours, minutes, seconds = convert_seconds(1000)
print(hours, minutes, seconds)

# Let's use tuples to store information about a file: its name, its type and
# its size in bytes. Fill in the gaps in this code to return the size in
# kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places.


def file_size(file_info):
    name, file_type, size_bytes = file_info
    return("{:.2f}".format(size_bytes / 1024))


print(file_size(('Class Assignment', 'docx', 17875)))  # Should print 17.46
print(file_size(('Notes', 'txt', 496)))  # Should print 0.48
print(file_size(('Program', 'py', 1239)))  # Should print 1.21
