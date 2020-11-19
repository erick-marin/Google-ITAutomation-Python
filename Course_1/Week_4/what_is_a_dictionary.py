"""
This script is used for course notes.

Author: Erick Marin
Date: 10/20/2020
"""

# Dictionaries = the data inside dictionaries take the form of pairs of keys
# and values. You can create an empty dictionary in a similar way to creating
# an empty list, except instead of square brackets dictionaries use curly
# brackets to define their content. Dictionaries are mutalble.

x = {}
print(type(x))

file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
print(file_counts)

print(file_counts["txt"])  # returns 14
print("jpg" in file_counts)  # returns true
print("html" in file_counts)  # returns false

# Add entry into dictionary
file_counts["cfg"] = 8
print(file_counts)

# When you use a key that already exists to set a value, the value that was
# already paired with that key is replaced.
file_counts["csv"] = 17
print(file_counts)

# We can delete elements from a dictionary with the del keyword by passing the
# dictionary and the key to the element as if we were trying to access it.
del file_counts["cfg"]
print(file_counts)

# The "toc" dictionary represents the table of contents for a book. Fill in the
# blanks to do the following: 1) Add an entry for Epilogue on page 39. 2)
# Change the page number for Chapter 3 to 24. 3) Display the new dictionary
# contents. 4) Display True if there is Chapter 5, False if there isn't.

toc = {"Introduction": 1, "Chapter 1": 4,
       "Chapter 2": 11, "Chapter 3": 25, "Chapter 4": 30}
toc["Epilogue"] = 39  # Epilogue starts on page 39
toc["Chapter 3"] = 24  # Chapter 3 now starts on page 24
print(toc)  # What are the current contents of the dictionary?
print("Chapter 5" in toc)  # Is there a Chapter 5?
