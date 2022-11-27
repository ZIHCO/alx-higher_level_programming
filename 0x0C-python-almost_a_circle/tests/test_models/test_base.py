#!/usr/bin/python3
"""Unittest for Base class"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Testcase for Base class"""

    def test__id(self):
        """Test the __init__ method"""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base(12).id, 12)
