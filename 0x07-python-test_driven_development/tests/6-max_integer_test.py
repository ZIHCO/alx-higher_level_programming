#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_arg(self):
        """argument test"""
        self.assertEqual(max_integer([2, 4, 5, 1]), 5)
        self.assertEqual(max_integer(), None)

    def test_type(self):
        """argument type"""
        self.assertRaises(TypeError, max_integer, "3") 
