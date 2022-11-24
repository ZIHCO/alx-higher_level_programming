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

    return dir(obj)
