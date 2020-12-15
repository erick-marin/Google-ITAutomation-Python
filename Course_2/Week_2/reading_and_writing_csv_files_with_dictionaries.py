"""
This script is used for course notes.

Author: Erick Marin
Date: 12/14/2020
"""

from os import write
import csv

with open("software.csv") as software:
    # If you have column field names in a csv file use the DictReader() which
    # creates each row into a dictionary allow to access data by using column
    # names instead of the postion in the row.
    reader = csv.DictReader(software)
    for row in reader:
        print(("{} has {} users").format(row["name"], row["users"]))

# Use DictWriter() in a similar method with each element being a row in a file.
users = [{"name": "Sol Mansi", "username": "solm", "department":
          "IT Infrastructure"},
         {"name": "Lio Nelson", "username": "lion",
          "department": "User Experience Research"},
         {"name": "Charlie Grey", "username": "greyc",
          "department": "Development"}]

# Define the list of keys to write to the file
keys = ["name", "username", "department"]

# Open th file for writing
with open("by_department.csv", "w") as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    # writeheader method will create the first row with the fieldname we
    # defined.
    writer.writeheader()
    writer.writerows(users)
