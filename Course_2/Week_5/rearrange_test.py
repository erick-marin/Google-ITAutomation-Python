#!/usr/bin/env python3

"""
This script is used for course notes.

Author: Erick Marin
Date: 12/21/2020
"""

# Import the function to be tested from the "rearrange" module.
from unittest.case import expectedFailure
from rearrange import rearrange_name
import unittest


class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase), expected)


unittest.main()
