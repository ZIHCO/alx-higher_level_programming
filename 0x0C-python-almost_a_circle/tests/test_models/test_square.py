#!/usr/bin/python3
"""This is the unittest for the module, Square."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests the square module"""

    def setUp(self):
        self.square1 = Square(2)

    def test_id(self):
        """test for id"""
        self.assertEqual(self.square1.id, 3)

    def test_validators(self):
        """validators of the setters"""
        with self.assertRaises(TypeError):
            self.square2 = Square(10, 'd', 1, 4)
        with self.assertRaises(ValueError):
            self.square2 = Square(10, -10, 1, 4)
    
    def test_area(self):
        """test for area"""
        self.assertEqual(self.square1.area(), 4)

    def test_display(self):
        """test for display"""
        self.assertEqual(self.square1.display(), None)

    def test_str(self):
        """test for __str__"""
        string = "[Square] (" + str(self.square1.id) + ") 0/0 - 2"
        self.assertEqual(self.square1.__str__(), string)

    def test_update(self):
        """test for update"""
        self.square1.update(10, 10, 1, 4)
        self.assertEqual(self.square1.id, 10)

    def test_size(self):
        """test for size"""
        self.assertEqual(self.square1.size, 2)
        self.square1.size = 10
        self.assertEqual(self.square1.size, 10)

    def test_to_dictionary(self):
        """test for to_dictionary"""
        self.assertEqual(self.square1.to_dictionary(),
                         {'id': self.square1.id, 'size': 2, 'x': 0,
                          'y': 0})
