#!/usr/bin/python3

"""
"4-from_json_string" module
contain the "from_json_string" function
"""


def from_json_string(my_str):
    """
    from_json_string - returns an object (Python data
    structure) represented by a JSON string

    Attributes:
        my_str: serialised obj to be deserialise

    Return:
        the json obj
    """
    import json

    my_str_obj = json.loads(my_str)
    return my_str_obj
