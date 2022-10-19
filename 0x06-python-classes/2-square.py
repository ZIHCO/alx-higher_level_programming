#!/usr/bin/python3
"""Square Class


Private instance attribute: size


"""


class Square:
    """Square Class

    Attributes:
        size: ...

    """

    def __init__(self, size=0):
        """__init__

        The __init__ method initializes the size value
        of the square.

        Attributes:
            size (int): The size of the square.

        """

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
