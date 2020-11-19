"""
This script is used for course notes.

Author: Erick Marin
Date: 10/20/2020
"""

# You can use for loops to iterate through the contents of a dictionary.
file_counts = {"jpg": 10, "txt": 14, "csc": 2, "py": 23}
for extension in file_counts:
    print(extension)

# If you want to access the associated values, you can either use the keys as
# indexes of the dictionary or you can use the items method which returns a
# tuple for each element in the dictionary. The tuple's first element is the
# key. Its second element is the value.

# We can use the .items method to get key, value pairs
for ext, amount in file_counts.items():
    print("There are {} files with the .{} extension". format(amount, ext))

# Sometimes you might just be interested in the keys of a dictionary. Other
# times you might just want the values. You can access both with their
# corresponding dictionary methods

# Use the keys() method to just get the keys
print(file_counts.keys())
# Use the values() method to just get the values
print(file_counts.values())

for value in file_counts.values():
    print(value)

# Complete the code to iterate through the keys and values of the cool_beasts
# dictionary. Remember that the items method returns a tuple of key, value
# for each element in the dictionary.

cool_beasts = {"octopuses": "tentacles", "dolphins": "fins", "rhinos": "horns"}
for beast, apendage in cool_beasts.items():
    print("{} have {}".format(beast, apendage))

# Dictionaries are a great tool for counting elements and analyzing frequency.


def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result


print(count_letters("aaaaa"))
print(count_letters("tenant"))
print(count_letters("a long string with a lot of letters"))
