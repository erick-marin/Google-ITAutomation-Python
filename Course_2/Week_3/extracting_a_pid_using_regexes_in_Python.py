"""
This script is used for course notes.

Author: Erick Marin
Date: 12/20/2020
"""

import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing \
    package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

result = re.search(
    regex, "A completely diffrent string that also has numbers [34567]")
print(result[1])

# If the search results returns a NoneType  object because it cannot find a
# match, use the following method to handle these errors.


# def extract_pid(log_line):
#     regex = r"\[(\d+)\]"
#     result = re.search(regex, log_line)
#     if result is None:
#         return ""
#     return result


# print(extract_pid(log))

# This will result in an empty string to handle any error if the regex search
# does not find a match.

# print(extract_pid("99 elephants in [cage]"))

# The regular expression used in the extract_pid function, to return the
# uppercase message in parenthesis, after the process id.


def extract_pid(log_line):
    regex = r"\[(\d+)\]:\s([A-Z]{0,})"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])


# 12345 (ERROR)
print(extract_pid(
    "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"))
print(extract_pid("99 elephants in a [cage]"))  # None
print(extract_pid(
    "A string that also has numbers [34567] but no uppercase message"))  # None
# 67890 (RUNNING)
print(extract_pid(
    "July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup"))
