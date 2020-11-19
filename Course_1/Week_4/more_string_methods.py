"""
This script is used for course notes.

Author: Erick Marin
Date: 10/11/2020
"""

# upper method
print("Mountains".upper())

# lower method
print("Mountains".lower())

answer = "YES"
if answer.lower() == "yes":
    print("User said yes")

# `strip` method will get rid of surrounding spaces in the string.
# 'strip` remove spaces, it also removes tabs and new line characters, which
# are all characters we don't usually want in user-provided strings.
strip_answer = " 'yes' ".strip()
print(strip_answer)

strip_left = " 'yes' ".lstrip()
print(strip_left)
strip_right = " 'yes' ".rstrip()
print(strip_right)

# `count` method returns how many times a given substring appears within a
# string.
count_string = "The number of times e occurs in this string is 4".count("e")
print(count_string)

# The method `endswith` returns whether the string ends with a certain substring.
endswith_string = "Forest".endswith("rest")
print(endswith_string)

# The method `isnumeric` returns whether the string's made up of just numbers.
# Adding to that, if we have a string that is numeric, we can use the int
# function to convert it to an actual number.
isnumeric_string = "Forest".isnumeric()
print(isnumeric_string)

isnumeric_string = "12345".isnumeric()
print(isnumeric_string)

# `join` method can also be used for concatenating
join_string = " ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"])
print(join_string)

join_string = "...".join(["This", "is", "a", "phrase", "joined", "by", \
                          "triple", "dots"])
print(join_string)

# `split` method can split a string into a list of strings.
# The split method returns a list of all the words in the initial string and
# it automatically splits by any whitespace. It can optionally take a
# parameter and split the strings by another character, like a comma or a dot.
split_string = "This is another example of split method".split()
print(split_string)

# Fill in the gaps in the `initials` function so that it returns the initials
# of the words contained in the phrase received, in upper case. For example:
# "Universal Serial Bus" should return "USB"; "local area network" should
# return "LAN”.


def initials(phrase):
    words = phrase.split()  # Creates a list by splitting words
    result = ""             # Empty string to build on
    for word in words:      # For each word in the words list
        result += word[0] # Strings are like lists of characters
    return result.upper()   # Convert result to uppercase


print(initials("Universal Serial Bus"))  # Should be: USB
print(initials("local area network"))  # Should be: LAN
print(initials("Operating system"))  # Should be: OS
