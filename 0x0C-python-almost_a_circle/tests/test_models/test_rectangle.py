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
