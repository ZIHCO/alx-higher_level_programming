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

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialises the private height and width attributes
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        type(self).number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method that returns the area"""
        return self.__height * self.__width

    def perimeter(self):
        """Public instance method that returns the perimeter"""
        if self.__height and self.__width:
            return 2 * (self.__height + self.__width)
        else:
            return 0

    def __str__(self):
        if self.__height and self.__width:
            return ((str(self.print_symbol) * self.__width + "\n")
                    * (self.__height - 1)
                    + (str(self.print_symbol) * self.width))
        return ""

    def __repr__(self):
        if self.__height and self.__width:
            return ("Rectangle(" + str(self.__width) + ", "
                    + str(self.__height) + ")")

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
