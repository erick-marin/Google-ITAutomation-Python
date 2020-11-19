"""
This script is used for course notes.

Author: Erick Marin
Date: 10/20/2020
"""

animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)

print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))

# The 'enumerate' function returns a tuple for each element in the list. The
# first value in the tuple is the index of the element in the sequence. The
# second value in the tuple is the element in the sequence.
winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))

# Try out the enumerate function for yourself in this quick exercise. Complete
# the skip_elements function to return every other element from the list, this
# time using the enumerate function to check if an element is on an even
# position or an odd position.


def skip_elements(elements):
    new_elements = []
    for element_index, element in enumerate(elements):
        # Becuase you are enumerating the list, no need for index += 1
        # to cycle the loop to the next index for evaulation.
        if element_index % 2 == 0:
            new_elements.append(element)
    return new_elements


# Should be ['a', 'c', 'e', 'g']
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
# Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))


def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result


print(full_emails([("alex@example.com", "Alex Diego"),
                   ("shay@example.com", "Shay Brandt")]))

# Because we use the range function so much with for loops, you might be
# tempted to use it for iterating over indexes of a list and then to access
# the elements through indexing. You could be particularly inclined to do this
# if you're used to other programming languages before. Because in some
# languages, the only way to access an element of a list is by using indexes.
# Real talk, this works but looks ugly. It's more idiomatic in Python to
# terate through the elements of the list directly or using enumerate when you
# need the indexes like we've done so far. There are some specific cases that
# do require us to iterate over the indexes, for example, when we're trying to
# modify the elements of the list we're iterating.
