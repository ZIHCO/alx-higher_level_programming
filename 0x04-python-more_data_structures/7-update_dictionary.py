#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for item in list(a_dictionary):
        if item == key:
            a_dictionary[item] = value
    else:
        a_dictionary[key] = value
    return a_dictionary
