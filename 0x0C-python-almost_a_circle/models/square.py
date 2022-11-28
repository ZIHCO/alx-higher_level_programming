#!/usr/bin/python3
"""square module contains the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class - inherit from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        Rectangle.__init__(self, size, size, x, y, id)
  
    def __str__(self):
        """override the __str__"""
        return ("[Square] " + "(" + str(self.id) + ") " + str(self.x)
                + "/" + str(self.y) + " - " + str(self.width))
