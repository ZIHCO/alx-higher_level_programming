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

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        if type(value) is not int:
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """area

        Returns:
            the current square area

        """
        return int(self.__size) * int(self.__size)
