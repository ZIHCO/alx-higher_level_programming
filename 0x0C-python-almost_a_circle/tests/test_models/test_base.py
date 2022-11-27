#!/usr/bin/python3
"""Unittest for Base class"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Testcase for Base class"""

    def setUp(self):
        """set up cases"""
        b1 = Base()
        b2 = Base()
        b3 = Base(12)

    def test__id(self):
        """Test the __init__ method"""
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)
