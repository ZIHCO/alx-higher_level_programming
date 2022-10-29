#!/usr/bin/python3
"""
"103-magic_class" module, contains the MagicClass
"""


class MagicClass:
    """The MagicClass"""

    def __init__(self, radius=0):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    import math

    def area(self):
        """returns the area of a circle"""
        return (math.pi**2) * self.__radius

    def circumference(self):
        """returns the circumference of a circle"""
        return 2 * math.pi * self.__radius
