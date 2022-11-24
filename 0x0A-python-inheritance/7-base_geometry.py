#!/usr/bin/python3
"""
6-base_geometry module contain the class
BaseGeometry
"""


class BaseGeometry:
    """BaseGeometry class

    Attributes:
        public instance method: def area
    """

    def area(self):
        """
        raises an exception message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validate value
        """
        if type(name) == str:
            self.name = name
            if type(value) is not int:
                raise TypeError(self.name + " must be an integer")
            if value <= 0:
                raise ValueError(self.name + " must be greater than 0")
