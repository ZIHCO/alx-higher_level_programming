#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a and tuple_b:
        len_a = len(tuple_a)
        len_b = len(tuple_b)
        if len_a == len_b:
            if len_a == 2:
                a1, b1 = tuple_a
                a2, b2 = tuple_b
            elif len_a == 1:
                a1, b1 = tuple_a[0], 0
                a2, b2 = tuple_b[0], 0
            else:
                a1, b1 = tuple_a[0], tuple_a[1]
                a2, b2 = tuple_b[0], tuple_b[1]
        elif len_a > len_b:
            if len_a == 2:
                a1, b1 = tuple_a
                a2, b2 = tuple_b[0], 0
            else:
                a1, b1 = tuple_a[0], tuple_a[1]
                if len_b == 1:
                    a2, b2 = tuple_b[0], 0
                else:
                    a2, b2 = tuple_b[0], tuple_b[1]
        else:
            if len_b == 2:
                a1, b1 = tuple_a[0], 0
                a2, b2 = tuple_b
            else:
                a2, b2 = tuple_b[0], tuple_b[1]
                if len_a == 1:
                    a1, b1 = tuple_a[0], 0
                else:
                    a1, b1 = tuple_a[0], tuple_a[1]
        sum_tuple = (a1 + a2, b1 + b2)
        return sum_tuple
    elif tuple_a:
        len_a = len(tuple_a)
        if len_a == 1:
            a1, b1 = tuple_a[0], 0
        else:
            a1, b1 = tuple_a[0], tuple_a[1]
        sum_tuple = (a1, b1)
        return sum_tuple
    elif tuple_b:
        len_b = len(tuple_b)
        if len_b == 1:
            a2, b2 = tuple_b[0], 0
        else:
            a2, b2 = tuple_b[0], tuple_b[1]
        sum_tuple = (a2, b2)
        return sum_tuple
    return (0, 0)
