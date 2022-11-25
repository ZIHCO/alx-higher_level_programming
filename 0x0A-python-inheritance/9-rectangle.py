#!/usr/bin/python3
"""
8-rectangle module contains the Rectangle class
that inherits from BaseGeometry
"""
Base_Geo = __import__('7-base_geometry').BaseGeometry


class Rectangle(Base_Geo):
    """
    Rectangle class inherits from BaseGeometry from the
    '7-base_geometry' module.

    Attributes:
        width: ....
        height: ...
    """

    def __init__(self, width, height):
        """instatiate with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """returns the description of the rectangle"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
