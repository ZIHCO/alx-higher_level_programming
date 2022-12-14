#!/usr/bin/python3
"""
rectangle module, contaains the subclass Rectangle that
inherits from the Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class - subclass of Base

    Attributes:
        __width
        __height
        __x
        __y
        __init__ - class constructor
    """

    # class constructor
    def __init__(self, width, height, x=0, y=0, id=None):
        """private instance attributes initiator"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, width):
        """set width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, height):
        """set height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, x):
        """set x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, y):
        """set y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """returns the area value of a rectangle instance"""
        return self.width * self.height

    def display(self):
        """print rectangle with char #"""
        print("\n" * self.y + (((" " * self.x + "#" * self.width) + "\n")
              * self.height), end="")

    def __str__(self):
        """override the __str__"""
        return ("[Rectangle] " + "(" + str(self.id) + ") " + str(self.x)
                + "/" + str(self.y) + " - " + str(self.width)
                + "/" + str(self.height))

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            arg_list = ["id", "width", "height", "x", "y"]
            i = 0
            while i < len(args):
                setattr(self, arg_list[i], args[i])
                i += 1
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dict rep for Rectangle"""
        attri_list = ["id", "width", "height", "x", "y"]
        i = 0
        dict_rect = {}
        while i < len(attri_list):
            dict_rect[attri_list[i]] = getattr(self, attri_list[i])
            i += 1

        return dict_rect
