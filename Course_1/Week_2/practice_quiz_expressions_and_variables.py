"""
This script is used for course notes.

Author: Erick Marin
Date: 10/07/2020
"""
# Practice Quiz: Expressions and Variables
#
# Question 1
# In this scenario, two friends are eating dinner at a restaurant. The bill
# comes in the amount of 47.28 dollars. The friends decide to split the bill
# evenly between them, after adding 15% tip for the service. Calculate the
# tip, the total amount to pay, and each friend's share, then output a message
# saying "Each person needs to pay: " followed by the resulting number.

BILL = 47.28
TIP = BILL * .15
TOTAL = BILL + TIP
SHARE = TOTAL / 2
print("Each person needs to pay: " + str(SHARE))

# Question 2
# This code is supposed to take two numbers, divide one by another so that the
# result is equal to 1, and display the result on the screen. Unfortunately,
# there is an error in the code. Find the error and fix it, so that the output
# is correct.
#
# numerator = 10
# denominator = 0
# result = numerator / denominator
# print(result)

NUMERATOR = 10
DENOMINATOR = 10
RESULT = NUMERATOR / DENOMINATOR
print(int(RESULT))

# Question 3
# Combine the variables to display the sentence "How do you like Python so
# far?"

WORD1 = "How"
WORD2 = "do"
WORD3 = "you"
WORD4 = "like"
WORD5 = "Python"
WORD6 = "so"
WORD7 = "far?"

print(WORD1 + " " + WORD2 + " " + WORD3 + " " + WORD4 + " " + WORD5 + " "
      + WORD6 + " " + WORD7)

# Question 4
# This code is supposed to display "2 + 2 = 4" on the screen, but there is an
# error. Find the error in the code and fix it, so that the output is correct.
#
# print("2 + 2 = " + (2 + 2))

print("2 + 2 = " + str(2 + 2))

# Question 5
print("What do you call a combination of numbers, symbols, or other values \
    that produce a result when evaluated?")

# An explicit conversion
# An expression
# A variable
# An implicit conversion

print("An expression")
