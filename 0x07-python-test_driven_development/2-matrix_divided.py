#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.

This module has one function, matrix_divided(). For example,
>>> matrix = [[1, 2, 3], [4, 5, 6]]

>>> matrix_divided(matrix, div)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """
    matrix_divided:
        return a new matrix, where each entry is
        a quotient of the entry of the input matrix
        divided div

    Attributes:
        a matrix of integers or floats and
        div an integer or float.

    Return:
        a new matrix
    """
    if (matrix):
        if type(matrix) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of"
                            " integers/floats")
        for row in matrix:
            if type(row) is not list:
                raise TypeError("matrix must be a matrix (list of lists) of"
                                " integers/floats")
        for row in matrix:
            for i in row:
                if type(i) not in (int, float):
                    raise TypeError("matrix must be a matrix (list of lists)"
                                    " of integers/floats")
        row_len = len(matrix[0])
        for row in matrix:
            if len(row) != row_len:
                raise TypeError("Each row of the matrix must have the size")
        if type(div) not in (int, float):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        return list(map(lambda i: list(map(lambda x: round((x / div), 2), i)),
                    matrix[:]))
