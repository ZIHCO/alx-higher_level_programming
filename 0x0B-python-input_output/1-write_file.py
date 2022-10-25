#!/usr/bin/python3

"""
"1-write_file" module
Contains the function "write_file"
"""


def write_file(filename="", text=""):
    """
    write_file:
        writes a string to a text file (UTF8)

    Attributes:
        takes two argument filename, and the text string to be written

    Return:
        the number of characters written
    """

    with open(filename, 'w', encoding="utf-8") as f:
        num_char = f.write(text)
        return num_char
