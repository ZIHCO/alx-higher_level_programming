#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy_list = my_list.copy()
    for i in copy_list:
        if i == search:
            index = copy_list.index(search)
            copy_list[index] = replace
    return copy_list
