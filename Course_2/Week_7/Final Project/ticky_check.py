#!/usr/bin/env python3

import re
import sys
import operator
import csv

per_user = {}
error = {}

logfile = open("syslog.log")

for logline in logfile:
    logline = logline.strip()
    username = (re.search(r"\((.*)\)", logline)).group(1)
    message = (re.search(r"(ERROR|INFO)", logline)).group(1)
    user_count = {"INFO": 0, "ERROR": 0}
    if (username not in per_user):
        per_user[username] = user_count
    per_user[username][message] += 1

    if message == "ERROR":
        system_error = (re.search(r"ERROR (.*) ", logline)).group(1)
        if (system_error not in error):
            error[system_error] = 0
        error[system_error] += 1
logfile.close()


sorted_per_user = []
sorted_error = []

for key in sorted(per_user.keys()):
    sorted_per_user.append(
        [key, per_user[key]["INFO"], per_user[key]["ERROR"]])

for key, value in sorted(error.items(), key=lambda item: item[1], reverse=True):
    sorted_error.append([key, value])

sorted_per_user.insert(0, ["Username", "INFO", "ERROR"])
sorted_error.insert(0, ["Error", "Count"])

error_messages_file = open("error_message.csv", "w")
user_statistics_file = open("user_statistics.csv", "w")

writer1 = csv.writer(error_messages_file)
writer1.writerows(sorted_error)

writer2 = csv.writer(user_statistics_file)
writer2.writerows(sorted_per_user)

error_messages_file.close()
user_statistics_file.close()
