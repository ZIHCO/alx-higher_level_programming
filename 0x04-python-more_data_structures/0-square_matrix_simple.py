#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squaredmat = []

    for row in matrix:
        arr = []
        for i in row:
            arr.append(i ** 2)
        squaredmat.append(arr)

    return squaredmat
