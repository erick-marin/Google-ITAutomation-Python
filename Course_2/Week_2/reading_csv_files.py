"""
This script is used for course notes.

Author: Erick Marin
Date: 12/14/2020
"""

import csv

file = open("csv_file.csv")
# reader() function of the csv module will interpret the file as a CSV
csv_file = csv.reader(file)
for row in csv_file:
    # Unpack row for values
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
file.close
