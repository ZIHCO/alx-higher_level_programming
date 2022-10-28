#!/usr/bin/python3
"""
"6-square" module. Contains the Square class
"""


class Square:
    """
    Square Class

    Attributes:
        size: private instance attribute
        position: private instance attribute
    """

    def __init__(self, size=0, position=(0, 0)):
        """__init__

        The __init__ method initializes the size value,
         and the position of the square.

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """size getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter method"""
        if type(value) is not int:
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """position getter method"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter method"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2"
                            " positive integers")
        elif (type(value[1]) is not int or type(value[0]) is not int):
            raise TypeError("position must be a tuple of 2"
                            " positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2"
                            " positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2"
                            " positive integers")
        else:
            self.__position = value

    def area(self):
        """area

        Returns:
            the current square area

        """
        return self.__size * self.__size

    def my_print(self):
        if self.__size:
            for i in range(self.__size):
                if i == 0:
                    print()
                if self.__position[0] > 0:
                    k = 0
                    while k < self.__position[0]:
                        print(" ", end="")
                        k += 1
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
