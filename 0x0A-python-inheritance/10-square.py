#!/usr/bin/python3
"""
10-square module contains the square class
that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle from the
    '9-rectangle' module.

    Attributes:
        size: ....
    """

    def __init__(self, size):
        """instatiate with size"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """returns the description of the rectangle"""
        return "[Rectangle] " + str(self.__size) + "/" + str(self.__size)
