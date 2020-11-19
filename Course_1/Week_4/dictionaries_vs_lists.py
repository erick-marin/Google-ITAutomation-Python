"""
This script is used for course notes.

Author: Erick Marin
Date: 10/21/2020
"""

# Think about the kind of information you can represent in each data structure.
# If you've got a list of information you'd like to collect and use in your
# script then the list is probably the right approach.

ip_addresses = ["192.168.1.1", "127.0.0.1", "8.8.8.8"]

# If you had a list of host names and their corresponding IP addresses, you
# might want to pair them as key values in a dictionary. Because of the way
# dictionaries work, it's super easy and fast to search for an element in them.
host_addresses = {"router": "192.168.1.1",
                  "localhost": "127.0.0.1", "google": "8.8.8.8"}

# In general, you want to use dictionaries when you plan on searching for a
# a specific element.

# You can use as dictionary keys an immutable data type:
# - Numbers
# - Booleans
# - Strings
# - Tuples
# But you can't use lists or dictionaries for that.
#
# The values associated with keys can be any type, including lists or even
# other dictionaries. You can use them to represent more complex data
# structures like directory trees in the file system.

# In Python, a dictionary can only hold a single value for a given key. To
# workaround this, our single value can be a list containing multiple values.
# Here we have a dictionary called "wardrobe" with items of clothing and
# their colors. Fill in the blanks to print a line for each item of clothing
# with each color, for example: "red shirt", "blue shirt", and so on.

wardrobe = {"shirt": ["red", "blue", "white"], "jeans": ["blue", "black"]}
for clothing_item, colors in wardrobe.items():
    for color in colors:
        print("{} {}".format(color, clothing_item))


# Set - Used when you want to store a bunch of elements and be certain that they're only present once.
# Elememnt of a set must also be immutable.
