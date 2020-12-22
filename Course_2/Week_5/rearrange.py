#!/usr/bin/env python3

"""
This script is used for course notes.

Author: Erick Marin
Date: 12/21/2020
"""

import re


def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    # This will handle the edge case if an empty string is in the result
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
