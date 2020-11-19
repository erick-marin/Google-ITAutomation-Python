"""
This script is used for course notes.

Author: Erick Marin
Date: 10/11/2020
"""

# You can think of lists as long boxes with the space inside the box divided
# up into different slots. Each slot can contain a different value.

x = ["Now", "we", "are", "cooking!"]

# data type
print(type(x))

# print out each element in the list.
print(x)

# using the len() function on a list returns the number of elements in a list
print(len(x))

# Check an element in a list with the in keyword, which will return a Boolean
print("are" in x)
print("Today" in x)

# Access individual elements in a list with indexing
# Can't access an element in  out of range index.
print(x[0])
print(x[3])

print(x[1:3])
print(x[:2])
print(x[2:])

# Using the "split" string method from the preceding lesson, complete the
# get_word function to return the {n}th word from a passed sentence. For
# example, get_word("This is a lesson about lists", 4) should return "lesson",
# which is the 4th word in this sentence. Hint: remember that list indexes
# start at 0, not 1.


def get_word(sentence, n):
    # Only proceed if n is positive
    if n > 0:
        words = sentence.split()
        # Only proceed if n is not more than the number of words
        if n <= len(words):
            return words[n - 1]
    return("")


print(get_word("This is a lesson about lists", 4))  # Should print: lesson
print(get_word("This is a lesson about lists", -4))  # Nothing
print(get_word("Now we are cooking!", 1))  # Should print: Now
print(get_word("Now we are cooking!", 5))  # Nothing

# String and lists are samples of sequences
# `for` element in sequence
# sequence[x]
# len(sequence)
# sequence + sequence
# element in sequence
