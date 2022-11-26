#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_arg(self):
        """argument test"""
        self.assertEqual(max_integer([2, 4, 5, 6]), 6)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-2, -3, -4]), -2)
        self.assertEqual(max_integer([-2, 0, 4]), 4)
        self.assertEqual(max_integer([2, -3, -4]), 2)
