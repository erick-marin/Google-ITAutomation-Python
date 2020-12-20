"""
This script is used for course notes.

Author: Erick Marin
Date: 12/19/2020
"""

import re

log = "July 31 07: 51: 48 mycomputer bad_process[12345]: ERROR Performing \
    package upgrade"
index = log.index("[")
print(log[index+1:index+6])

# using the regex module
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])
