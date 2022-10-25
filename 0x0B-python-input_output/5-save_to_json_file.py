#!/usr/bin/python3

"""
"5-save_to_json_file" module
contains onefunction, "save_to_json_file"
"""


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file - writes an Object to a text file,
    using a JSON representation

    Attributes:
        my_obj: object to write to file
        filename: file to write to

    Return:
        void
    """

    import json

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
