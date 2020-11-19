"""
This script is used for course notes.

Author: Erick Marin
Date: 10/11/2020
"""

# `format` method with curly brackets place holder
firstname = "Manny"
number = len(firstname) * 3
print("Hello {}, your lucky number is {}".format(firstname, number))

print("Your lucky number is {number}, {firstname}.".format(
    firstname=firstname, number=len(firstname)*3))

# Modify the student_grade function using the format method, so that it
# returns the phrase "X received Y% on the exam". For example, student_grade
# ("Reed", 80) should return "Reed received 80% on the exam".


def student_grade(name, grade):
    return "{} recieved {}% on the exam.".format(name, grade)


print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

# Writing a formatting expression
price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))


def to_celsius(x):
    return (x - 32) * 5 / 9


# In the first expression we're saying we want the numbers to be aligned to
# the right for a total of three spaces. In the second expression we're saying
# we want the number to always have exactly two decimal places and we want to
# align it to the right at six spaces.

for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
