#!/usr/bin/python3
"""Unittest for Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Testcase for Base class"""

    def setUp(self):
        """set up cases"""
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(12)

    def tearDown(self):
        """tear down"""
        pass

    def test__id(self):
        """Test the __init__ method"""
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 12)
