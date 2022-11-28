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

    @property
    def size(self):
        """get atrribute"""
        return self.width

    @size.setter
    def size(self, value):
        """set attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update square by assigning attributes"""
        if args:
            args_list = ["id", "size", "x", "y"]
            i = 0
            while i < len(args):
                setattr(self, args_list[i], args[i])
                i += 1
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
