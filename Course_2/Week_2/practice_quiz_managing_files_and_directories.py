"""
This script is used for course notes.

Author: Erick Marin
Date: 11/28/2020
"""

# Practice Quiz: Managing Files and Directories

import os
import datetime

# 1. The create_python_script function creates a new python script in the
# current working directory, adds the line of comments to it declared by the
# 'comments' variable, and returns the size of the new file. Fill in the gaps
# to create a script called "program.py".


def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, "w") as file:
        file.write(comments)
        filesize = os.path.getsize(
            "/home/k/Documents/Devs/Google-ITAutomation-Python/" + filename)
    return(filesize)


print(create_python_script("program.py"))

# 2. The new_directory function creates a new directory inside the current
# working directory, then creates a new empty file inside the new directory,
# and returns the list of files in that directory. Fill in the gaps to
# create a file "script.py" in the directory "PythonPrograms".


def new_directory(directory, filename):
    # Before creating a new directory, check to see if it already exists
    if os.path.isdir(
        "/home/k/Documents/Devs/Google-ITAutomation-Python/Course_2/Week_2/"
            + directory) is False:
        os.mkdir(
            "/home/k/Documents/Devs/Google-ITAutomation-Python/Course_2/"
            "Week_2/" + directory)
    # Create the new file inside of the new directory
    os.chdir(
        "/home/k/Documents/Devs/Google-ITAutomation-Python/Course_2/Week_2/"
        + directory)
    with open(filename, "w") as file:
        pass
    # Return the list of files in the new directory
    return os.listdir(".")


print(new_directory("PythonPrograms", "script.py"))

# 3. Which of the following methods from the os module will create a new
# directory?

# [ ] path.isdir()
# [ ] listdir()
# [x] mkdir()
# [ ] chdir()

# 4. The file_date function creates a new file in the current working
# directory, checks the date that the file was modified, and returns
# just the date portion of the timestamp in the format of yyyy-mm-dd. Fill in
# the gaps to create a file called "newfile.txt" and check the date that it
# was modified.


def file_date(filename):
    # Create the file in the current directory
    with open(filename, "w") as file:
        timestamp = os.path.getmtime(filename)
    # Convert the timestamp into a readable format, then into a string
        datestamp = datetime.datetime.fromtimestamp(timestamp)
    # Return just the date portion
    return ("{:.10}".format(str(datestamp)))


print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd

# 5. The parent_directory function returns the name of the directory that's
# located just above the current working directory. Remember that '..' is a
# relative path alias that means "go up to the parent directory". Fill in
# the gaps to complete this function.


def parent_directory():
    # Create a relative path to the parent
    # of the current working directory
    relative_parent = os.path.join(os.getcwd(), "../")
    # relative_parent = os.path.join(os.getcwd(), os.pardir)
    # Return the absolute path of the parent directory
    return os.path.abspath(relative_parent)


print(parent_directory())
