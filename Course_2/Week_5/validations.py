#!/usr/bin/env python3

"""
This script is used for course notes.

Author: Erick Marin
Date: 12/26/2020
"""


def validate_user(username, minlen):
    # An alternative to the raise keyword that we can use for situations where
    # we want to check that our code behaves the way it should particularly
    # when we want to avoid situations that should never happen. This is the
    # assert keyword. This keyword tries to verify that a conditional
    # expression is true, and if it's false it raises an assertion error with
    # the indicated message.

    assert type(username) == str, "username must be a string"
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True
