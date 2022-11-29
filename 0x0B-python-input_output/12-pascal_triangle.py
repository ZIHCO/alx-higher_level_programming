#!/usr/bin/python3
"""12-pascal_triangle contains the function
pascal_triangle
"""


def pascal_triangle(n):
    """returns a list of lists of integers"""

    new_list = []
    if n > 0:
        m = 1
        if n > 1:
            while m <= n:
                i = 0
                sub_list = []
                while i < m:
                    if i == 0:
                        sub_list.append(1)
                    elif (i + 1) == m:
                        sub_list.append(1)
                    else:
                        sub_list.append((last_list[i - 1]
                                        + last_list[i]))
                    i += 1
                last_list = sub_list[:]
                new_list.append(sub_list)
                m += 1
            return new_list

    return new_list
