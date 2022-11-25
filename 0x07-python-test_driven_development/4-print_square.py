#!/usr/bin/python3
"""
4-print_square module contains print_square
"""


def print_square(size):
    """prints a square with #"""
    if size:
        if type(size) is int and size < 0:
            raise ValueError("size must be >= 0")
        if size == int(size) and size < 0:
            raise TypeError("size must be an integer")
        elif size == int(size):
            size = int(size)
        if type(size) is not int:
            raise TypeError("size must be an integer")
        print(((("#" * size) + "\n") * size), end="")
