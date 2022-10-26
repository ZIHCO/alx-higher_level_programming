#!/usr/bin/python3

"""
"6-load_from_json_file" module
contains the "load_from_json_file" function
"""


def load_from_json_file(filename):
    """
    load_from_json_file - that creates an Object from a “JSON file”

    Attributes:
        filename - the json file to create object from

    Return:
        void
    """
    import json

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
