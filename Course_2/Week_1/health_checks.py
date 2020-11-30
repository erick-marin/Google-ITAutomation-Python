#!/usr/bin/env python3
"""
This script is used for course notes.

Author: Erick Marin
Date: 11/30/2020
"""

import shutil
import psutil

# Define a check_disk_usage function that will receive a disk usage check and
# return true if there's more than 20 percent free or false if it's less.


def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

# Define a cpu check usage for a whole second. We'll say the machine is
# healthy, if the cpu_usage is less than 75 percent.


def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75


if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!")
else:
    print("Everthing is OK!")
