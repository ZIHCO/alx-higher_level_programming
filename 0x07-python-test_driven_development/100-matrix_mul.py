#!/usr/bin/python3
"""This module, 100-matrix_mul contains the the definition,
   matrix_mul.
"""


def matrix_mul(m_a, m_b):
    """returns the dot product of two matrices"""
    if not (m_a and m_b):
        return None
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if type(m_a[0]) is not list:
        raise TypeError("m_a must be a list of lists")
    if type(m_b[0]) is not list:
        raise TypeError("m_b must be a list of lists")
    if len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
            if i != i:
                raise ValueError("m_a contains NaN")
            if i in [float('inf'), -(float('inf'))]:
                raise ValueError("m_a contains infinity")
    for row in m_b:
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
            if i != i:
                raise ValueError("m_b contains NaN")
            if i in [float('inf'), -(float('inf'))]:
                raise ValueError("m_b contains infinity")
    m_a_column = len(m_a[0])
    for row in m_a:
        if m_a_column != len(row):
            raise TypeError("each row of m_a must be of the same size")
    m_b_column = len(m_b[0])
    for row in m_b:
        if m_b_column != len(row):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = []
    transposed_m_b = [[row[i] for row in m_b] for i in range(len(m_b[0]))]

    for row in m_a:
        result_row = []
        for row_t in transposed_m_b:
            new_entry = 0
            for i in range(len(transposed_m_b[0])):
                new_entry += (row[i] * row_t[i])
            result_row.append(new_entry)
        result.append(result_row)

    return result
