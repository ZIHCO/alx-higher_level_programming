#!/usr/bin/python3
"""Uses numpy to perform dot product on matrices"""


def lazy_matrix_mul(m_a, m_b):
    """return dot product of m_a and m_b"""
    import numpy
    """returns the dot product of m_a and m_b"""
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

    return numpy.dot(m_a, m_b)
