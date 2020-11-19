"""
This script is used for course notes.

Author: Erick Marin
Date: 10/05/2020
"""
# Keeping in mind there are 86400 seconds per day, write a program that
# calculates how many seconds there are in a week, if a week is 7 days. Print
# the result on the screen.

print(86400 * 7)

# Calculate how many different passwords can be formed with 6 lower case
# English letters. For a 1 letter password, there would be 26 possibilities.
# For a 2 letter password, each letter is independent of the other, so there
# would be 26 times 26 possibilities. Using this information, print the amount
# of possible passwords that can be formed with 6 letters.

print(26**6)

# Most hard drives are divided into sectors of 512 bytes each. Our disk has a
# size of 16 GB. Fill in the blank to calculate how many sectors the disk has.

DISK_SIZE = 16*1024*1024*1024
SECTOR_SIZE = 512
SECTOR_AMOUNT = DISK_SIZE / SECTOR_SIZE

print(SECTOR_AMOUNT)
