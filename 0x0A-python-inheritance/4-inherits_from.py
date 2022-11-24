#!/usr/bin/python3
"""
4-inherits_from module. Contains inherits_from
"""


def inherits_from(obj, a_class):
    """Returns - a bool if obj iherits directly or indirectly
       from the specified class
    """

    if isinstance(type(obj), a_class) or type(obj) != a_class:
        return True
    return False
