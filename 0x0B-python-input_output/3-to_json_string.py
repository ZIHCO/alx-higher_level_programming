#!/usr/bin/python3

"""
"3-to_json_string" module
contains the "to_json_string" function
"""


def to_json_string(my_obj):
    """
    to_json_string -  returns the JSON representation of an
    object (string)

    Attributes:
        my_obj - object to serialise

    Return:
         returns the JSON representation of an object (string)
    """

    import json

    str_my_obj = json.dumps(my_obj)
    return str_my_obj
