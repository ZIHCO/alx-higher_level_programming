#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    length = 0
    for row in matrix:
        for j in row:
            length = len(row)
            if row.index(j) == length - 1:
                print("{:d}".format(j))
            else:
                print("{:d}".format(j), end=' ')
    if length == 0:
        print(f"")
