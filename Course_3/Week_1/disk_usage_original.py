#!/usr/bin/env python3

"""
This script is used for course notes.

Author: Erick Marin
Date: 01/06/2020
"""

import shutil


def check_disk_usage(disk, min_absolute, min_percent):
    """Returns True if there is enough free disk space, false otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_absolute:
        return False
    return True


# Check for at least 2 GB and 10% free
if not check_disk_usage("/", 2*2**30, 10):
    print("ERROR : Not enough disk space")
    return 1


print("Everything OKAY")
return 0
