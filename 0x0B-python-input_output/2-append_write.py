#!/usr/bin/python3
"""
The "2-append_write" module.
Contains the "append_write" function
"""


def append_write(filename="", text=""):
    """
    append_write:
         appends a string at the end of a text file (UTF8)

    Attributes:
        filename the file to append to
        text the string to append

    Return:
         returns the number of characters added
    """

    with open(filename, 'a', encoding="utf-8") as f:
        num_char = f.write(text)
        return num_char
