#!/usr/bin/python3
"""
base module contains the Base class
"""
import json


class Base:
    """
    Base class: manage id attribute in all the subclass

    Attributes:
        __nb_objects - class attribute initialized with 0
        __init__ - class constructor
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """assign the public instance attribute id"""

        if id:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string repr"""
        if list_dictionaries:
            return json.dumps(list_dictionaries, separators=(':', ','))
        return "[]"
