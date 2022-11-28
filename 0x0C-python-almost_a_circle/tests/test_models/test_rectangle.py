#!/usr/bin/python3
"""Unittest for Rectangle class"""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Testcase for Rectangle class"""

    def setUp(self):
        """rectangle setup"""
        self.r1 = Rectangle(2, 20)
        self.r2 = Rectangle(3, 10)
        self.r3 = Rectangle(12, 2, 0, 3, 23)

    def test__id(self):
        """Test the __init__ method"""
        self.assertEqual(self.r3.id, 23)
        self.assertEqual(self.r1.id, 3)
        self.assertEqual(self.r2.id, 4)

    def test_validator(self):
        """Test for the setter and getter validator"""
        with self.assertRaises(ValueError):
            self.r1.width = -10
        with self.assertRaises(TypeError):
            self.r2.height = "10"
        with self.assertRaises(TypeError):
            self.r3.x = {}
        with self.assertRaises(ValueError):
            self.r3.y = -1
