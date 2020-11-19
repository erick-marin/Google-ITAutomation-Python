"""
This script is used for course notes.

Author: Erick Marin
Date: 10/12/2020
"""

# The following code will produce a TypeError: 'int' object not iterable

# for x in 25:
#     print()

# To correct this issue:
for x in range(25):
    print(x)

# This will print out 0, 1, 2, 3, ..., 24.

# If you want to iterate over a list with only one element then use the
# 'list' data structure by having value(s) within brackets [].

for x in [25]:
    print(x)


def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)


greet_friends(["Taylor", "Luisa", "Jamaal", "Eli"])

# What if you do not pass a list of paramters to the for loop function?

greet_friends("Barry")

# Even though a list of items was not passed to the function, it looped
# throught the string parameter sent to the function.  That's becuase
# strings are iterable.

# The validate_users function is used by the system to check if a list of
# users is valid or invalid. A valid user is one that is at least 3 characters
# long. For example, ['taylor', 'luisa', 'jamaal'] are all valid users. When
# calling it like in this example, something is not right. Can you figure out
# what to fix?


# def validate_users(users):
#    for user in users:
#        if is_valid(user):
#            print(user + " is valid")
#        else:
#            print(user + " is invalid")


# validate_users("purplecat")

def is_valid(name):
    strLength = len(name)
    print("Length of string is " + str(strLength) + " characters.")
    if strLength >= 3:
        return True


def validate_users(users):
    for user in users:
        if is_valid(user):
            print(user + " is valid")
        else:
            print(user + " is invalid")


validate_users(["purplecat"])
