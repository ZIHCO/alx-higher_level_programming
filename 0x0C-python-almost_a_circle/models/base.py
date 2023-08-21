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
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string repr of list_objs to a file"""
        list_dict = []
        if list_objs:
            for i in list_objs:
                list_dict.append(i.to_dictionary())
        objs_json = cls.to_json_string(list_dict)
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(objs_json)

    @staticmethod
    def from_json_string(json_string):
        """deserialises the json obj and returns the python object"""
        import json

        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attr already set"""
        if not dictionary:
            return cls
        if cls.__name__ == "Rectangle":
            rectangle = cls(1, 1)
            rectangle.update(**dictionary)
            return rectangle
        square = cls(1)
        square.update(**dictionary)
        return square

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        import os

        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r", encoding='utf-8') as f:
            json_str = f.read()
            list_dict = cls.from_json_string(json_str)
        list_obj = []
        for item in list_dict:
            instance = cls.create(**item)
            list_obj.append(instance)
        return list_obj
