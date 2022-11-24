#!/usr/bin/python3
"""
3-is_kind_of_class is a module contain the function definition
is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """Returns - a bool if obj an instance of a_class directly, or
       indirectly
    """

    if isinstance(obj, a_class):
        return True
    return False
