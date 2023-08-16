#!/usr/bin/python3
"""This module contains the function, append_after"""


def append_after(filename="", search_string="", new_string=""):
    """append_after insert a line of text after the search_string"""
    with open(filename, 'r', encoding='utf-8') as f:
        string = f.readline()
        write_list = []
        while string != "":
            make_list = string.split()
            """if "Holberton" in make_list:
                idx = make_list.index("Holberton")
                make_list.pop(idx)
                make_list[-1] = make_list[-1] + "\n"
                new_str = " ".join(make_list)
                write_list.append(new_str)
                string = f.readline()
                continue"""
            if search_string in string:
                write_list.append(string)
                write_list.append(new_string)
            else:
                write_list.append(string)
            string = f.readline()
    with open(filename, 'w', encoding='utf-8') as f:
        new_content = "".join(write_list)
        f.write(new_content)
