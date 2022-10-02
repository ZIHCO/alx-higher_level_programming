#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    length = 0
    for row in matrix:
        for j in row:
            length = len(row) - 1
            if row.index(j) == length:
                print("{:d}".format(j))
            else:
                print("{:d}".format(j), end=' ')
    if length == 0:
        print(f"")
