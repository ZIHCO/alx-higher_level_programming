#!/usr/bin/python3
"""Unittest for Rectangle class"""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Testcase for Rectangle class"""

    def test__id(self):
        """Test the __init__ method"""
        self.assertEqual(Rectangle(12, 2, 0, 3, 23).id, 23)
        self.assertEqual(Rectangle(2, 20).id, 1)
        self.assertEqual(Rectangle(3, 10).id, 2)

    def test_validator(self):
        """Test for the setter and getter validator"""
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.width = -10
        with self.assertRaises(TypeError):
            r.height = "10"
        with self.assertRaises(TypeError):
            r.x = {}
        with self.assertRaises(ValueError):
            r.y = -1
