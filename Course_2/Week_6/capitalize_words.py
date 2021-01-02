#!/usr/bin/env python3

"""
This script is used for course notes.

Author: Erick Marin
Date: 01/01/2021
"""

import sys

for line in sys.stdin:
    words = line.strip().split()
    print(" ".join([word.capitalize() for word in words]))
