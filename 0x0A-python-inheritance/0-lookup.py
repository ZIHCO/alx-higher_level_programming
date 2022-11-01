#!/usr/bin/python3
"""
The "lookup" module, it contains the lookup
function.
"""


def lookup(obj):
    """
    lookup - returns the list of available attributes and
    methods of an object.

    Argument:
        obj: the object to lookup

    Return:
        list object
    """

    obj_dict = obj.__dict__
    obj_dict_keys = []
    for key in obj_dict:
        obj_dict_keys = obj_dict_keys + [key]

    return obj_dict_keys
