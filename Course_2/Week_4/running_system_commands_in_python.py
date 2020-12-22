"""
This script is used for course notes.

Author: Erick Marin
Date: 12/21/2020
"""

import subprocess

# command-line arguments within brackets
subprocess.run(["date"])

# The parent process (script) can not complete until the child process
# run() is completed.
subprocess.run(["sleep", "2"])

# This will return the return code attirbute of process requested.
result = subprocess.run(["ls", "this_file_does_not_exist"])
print("Return code is: " + str(result.returncode))

subprocess.run(["ping", "-c", "1", "www.google.com"])
