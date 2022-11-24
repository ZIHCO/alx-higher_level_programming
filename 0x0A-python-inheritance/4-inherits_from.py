#!/usr/bin/python3
"""
4-inherits_from module. Contains inherits_from
"""


def inherits_from(obj, a_class):
    """Returns - a bool if obj iherits directly or indirectly
       from the specified class
    """

    if isinstance(obj, a_class) and \
       issubclass(a_class, obj.__class__) is False:
        return True
    return False
