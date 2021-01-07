#!/usr/bin/env python3
"""
This script is used for course notes.

Author: Erick Marin
Date: 01/06/2021
"""

import re


def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result is None:
        return result
    return "{} {}".format(result[2], result[2])
