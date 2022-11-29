#!/usr/bin/python3
"""8-class_to_json module, containing class_to_json function"""


def class_to_json(obj):
    """returns the dictionary description for JSON serialization
    """
    return obj.__dict__
