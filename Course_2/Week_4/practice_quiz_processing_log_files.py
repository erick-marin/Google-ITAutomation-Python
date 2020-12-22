"""
This script is used for course notes.

Author: Erick Marin
Date: 12/21/2020
"""

# Practice Quiz: Processing Log Files
#
# 1. You have created a Python script to read a log of users running CRON jobs.
# The script needs to accept a command line argument for the path to the log
# file. Which line of code accomplishes this?

# [ ] import sys
# [x] syslog = sys.argv[1]
# [ ] print(line.strip())
# [ ] usernames = {}

# 2. Which of the following is a data structure that can be used to count how
# many times a specific error appears in a log?
#
# [ ] Get
# [x] Dictionary
# [ ] Search
# [ ] Continue

# 3. Which keyword will return control back to the top of a loop when
# iterating through logs?
#
# [x] Continue
# [ ] Get
# [ ] With
# [ ] Search

# 4. When searching log files using regex, which regex statement will search
# for the alphanumeric word "IP" followed by one or more digits wrapped in
# parentheses using a capturing group# ?
#
# [ ] r"IP \(\d+\)$"
# [ ] b"IP \((\w+)\)$"
# [x] r"IP \((\d+)\)$"
# [ ] r"IP \((\D+)\)$"

# 5. Which of the following are true about parsing log files? (Select all that
# apply.)
#
# [ ] Load the entire log files into memory.
# [x] You should parse log files line by line.
# [x] It is efficient to ignore lines that don't contain the information we
#     need.
# [x] We have to open() the log files first.
