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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        Base.__init__(self, id)

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, width):
        """set width"""
        self.__width = width

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, height):
        """set height"""
        self.__height = height

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, x):
        """set x"""
        self.__x = x

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def width(self, y):
        """set y"""
        self.__y = y
