#!/usr/bin/python3
"""
"1-rectangle" module containing the "Rectangle" class
"""


class Rectangle:
    """
    Rectangle Class

    Attributes:
        width: attribute of the Rectangle
        height: ...
    """

    def __init__(self, width=0, height=0):
        """
        Initialises the private height and width attributes
        """
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(width) is not int:
            raise TypeError("width must be an integer")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(width) is not int:
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if value < 0:
            raise ValueError("height must be >= 0")
        if type(value) is not int:
            raise TypeError("height must be an integer")
        self.__height = value
