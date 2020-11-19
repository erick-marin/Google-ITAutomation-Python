"""
This script is used for course notes.

Author: Erick Marin
Date: 10/11/2020
"""

# Strings in Python are immutable.  Meaning that they can't be modified.
message = "A kong string with a stilly typo"

# To modify a new string

new_message = message[0:2] + "l" + message[3:]
print(new_message)

# We can assign a new value to the same variable 'message'.  The
# assignment of a string is mutable.
message = "This is a new message"
print(message)
message = "And another one"
print(message)

# In this case, we're using a method to get the index of a certain character.
# A method is a function associated with a specific class. We can call a
# method by following the variable with a dot.
pets = "Cats & Dogs"
print(pets.index("&"))
print(pets.index("Dog"))

# The 'index' method returns only the first position that matches.
print(pets.index("s"))

# And what happens if the string doesn't have the substring we're looking for?
# The `index` method can't return a number because the substring isn't there, so
# we get a value error instead.

# print(pets.index("x"))
#
# Traceback....
# ValueError: substring not found

# Using the index method, find out the position of "x" in
# "supercalifragilisticexpialidocious".

word = "supercalifragilisticexpialidocious"
print(word.index("x"))

# How can we know if a substring is contained in a string to avoid the error?
# We can use the keyboard in to check if a substring is contained in a string.
# We came across the keyword in, when using four loops. In that case, it was
# used for iteration. Here, it's a conditional that can be either true or
# false. It'll be true if the substring is part of the string, and false if
# it's not.

# Should return False
"Dragons" in pets

# Should return True
"Cats" in pets

# Funtion to replace old domain with new domain name.


def replace_domain(email, old_domain, new_doamin):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_doamin
        return new_email
    return email


print(replace_domain("erick.marin@dvs.net", "dvs.net", "internetworks.io"))
