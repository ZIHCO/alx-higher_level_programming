#!/usr/bin/python3
"""
This is the "0-read-file" module.
It contains the "read_file" function.
"""

def read_file(filename=""):
    """
    read_file:
        reads a text file (UTF8) and prints it to stdout

    Attributes:
        takes a stringed filename as argument

    Return:
        nothing
    """

    if (filename):
        with open(filename, encoding="utf-8") as f:
            for line in f:
                print(line, end="")
