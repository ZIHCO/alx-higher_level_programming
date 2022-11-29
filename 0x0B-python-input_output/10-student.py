#!/usr/bin/python3
"""9-student module contains the Student class"""


class Student:
    """
    Student class

    Attributes:
        public instance attributes - first_name, last_name, age

        __init__ - first_name, last_name, age

        to_json - public method that retrieves a dict rep from
        student
    """

    def __init__(self, first_name, last_name, age):
        """instantiate attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dict repr"""
        if attrs is not None:
            new_dict = {}
            i = 0
            while i < len(attrs):
                if attrs[i] in list(self.__dict__):
                    new_dict[attrs[i]] = self.__dict__[attrs[i]]
                i += 1
            return new_dict

        return self.__dict__
