"""
This script is used for course notes.

Author: Erick Marin
Date: 10/11/2020
"""

# append method; add item at the end
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")
print(fruits)

# insert method: adds item at the index indicated
# If you use an index higher than the current element lenght the item jsut
# gets added to the end.
fruits.insert(0, "Orange")
print(fruits)
fruits.insert(25, "Peach")
print(fruits)

# remove method removes the first occurence in the list
fruits.remove("Melon")
print(fruits)

# pop method returns the element that was removed at the index that was passed
fruits.pop(3)
print(fruits)

# The last way to modify the contents of a list is to change an item by
# assigning something else to that position.
fruits[2] = "Strawberry"
print(fruits)

# The skip_elements function returns a list containing every other element
# from an input list, starting with the first element. Complete this function
# to do that, using the for loop to iterate through the input list.


def skip_elements(elements):
    # Initialize variables
    new_list = []
    i = 0

    # Iterate through the list
    for element in elements:
        # Does this element belong in the resulting list?
        if i % 2 == 0:
            # Add this element to the resulting list
            new_element = elements[i]
            new_list.append(new_element)
        # Increment i
        i += 1
    return new_list


# Should be ['a', 'c', 'e', 'g']
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
# Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))
print(skip_elements([]))  # Should be []
