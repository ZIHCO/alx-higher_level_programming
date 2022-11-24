#!/usr/bin/python3
"""
2-is_same_class module, contain a function is_same_class
"""


def is_same_class(obj, a_class):
    """Returns a bool if obj is an instance of a_class"""
    if type(obj) == a_class:
        return True
    return False
