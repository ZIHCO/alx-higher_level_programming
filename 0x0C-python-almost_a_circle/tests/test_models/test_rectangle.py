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

    def tearDown(self):
        """tear down"""
        pass

    def test__value(self):
        """Test the __init__ method"""
        self.assertEqual(self.r3.id, 23)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r2.height, 10)

    def test_validator(self):
        """Test for the setter and getter validator"""
        with self.assertRaises(ValueError):
            self.r6 = Rectangle(1, -10, 0, 0, 6)
        with self.assertRaises(TypeError):
            self.r4 = Rectangle(1, 1, 1, "10", 13)
        with self.assertRaises(TypeError):
            self.r5 = Rectangle(1, 2, {}, 1, 5)
        with self.assertRaises(ValueError):
            self.r = Rectangle(0, 2, 0, 3, 21)

    def test_area(self):
        """Test for area"""
        self.assertEqual(self.r1.area(), 40)

    def test_display(self):
        """test for display"""
        self.assertEqual(Rectangle(1, 1).display(), print("#", end=''))
