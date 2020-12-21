#!/usr/bin/env python3

"""
This script is used for course notes.

Author: Erick Marin
Date: 12/19/2020
"""

import os
import sys

# filename that recieves a command line argument.
# ./script_name <arg>
filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("New file created\n")

else:
    print("Error, the file {} already exists!".format(filename))
    sys.exit(1)
