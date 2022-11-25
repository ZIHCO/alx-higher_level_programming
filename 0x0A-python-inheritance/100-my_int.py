#!/usr/bin/python3
"""
100-my_int module contains MyInt class
"""


class MyInt(int):
    """
    MyInt inherits the int class
    """
    def __eq__(self, value):
        """invert == with !="""
        return int(self) != int(value)

    def __ne__(self, value):
        """invert != with =="""
        return int(self) == int(value)
