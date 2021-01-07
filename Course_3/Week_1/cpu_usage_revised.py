#!/usr/bin/env python3

"""
This script is used for course notes.

Author: Erick Marin
Date: 01/06/2020
"""

import psutil


def check_cpu_usage(percent):
    usage = psutil.cpu_percent(1)
    print("DEBUG: usage: {}".format(usage))
    return usage < percent


if not check_cpu_usage(75):
    print("ERROR! CPU is overloaded")
else:
    print("Everything ok")
