#!/usr/bin/python3
"""
This is the "0-add_integer" module.

This module has one function, add_integer(). For example,

>>> add_integer(4, 5)
9
"""


def add_integer(a, b=98):
    """add_integer

    sum two int/float value

    Attributes:
        a and b are integer or float.

    Return:
        the sum of a and b, where a and b can be
        integers or floatand integer.
    """
    if a or a == 0:
        if type(a) is not int and type(a) is not float:
            raise TypeError("a must be an integer")
        if type(b) is not int and type(b) is not float:
            raise TypeError("b must be an integer")
        return int(a) + int(b)
    raise TypeError("a must be an integer")
