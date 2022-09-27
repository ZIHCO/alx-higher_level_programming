#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy_list = my_list.copy()
    if idx < len(my_list) and idx > 0:
        cpy_list[idx] = element
    return cpy_list
