"""
This script is used for course notes.

Author: Erick Marin
Date: 10/28/2020
"""
import PIL.Image
import pandas

image = PIL.Image.open("Course_2/Week_1/FujiFilm_Shots.jpg")
print(image.size)
print(image.format)

visitors = [1235, 6424, 9345, 8464, 2345]
errors = [23, 45, 33, 45, 76]

# Generate a DataFrame, the main structure used by Pandas for data analysis
df = pandas.DataFrame({"visitors": visitors, "errors": errors},
                      index=["Mon", "Tues", "Wed", "Thu", "Fri"])
print(df)

average_errors = df["errors"].mean()
print(average_errors)
