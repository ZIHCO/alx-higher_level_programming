#!/usr/bin/python3
"""This script reads from stdin"""
from sys import stdin


def print_status_count():
    print(f"File size: {file_size}")
    list_code = list(sorted(line_dict))
    for item in list_code:
        if line_dict[item] != 0:
            print(f"{int(item)}: {int(line_dict[item])}")


i = 0
file_size = 0
line_dict = {"200": 0, "301": 0, "400": 0, "401": 0,
             "403": 0, "404": 0, "405": 0, "500": 0}
try:
    for line in stdin:
        if i % 10 == 0 and i != 0:
            print_status_count()
            i = 0
        line_list = line.split()
        file_size += int(line_list[-1])
        line_dict[line_list[-2]] += 1
        i += 1
    print_status_count()
except KeyboardInterrupt:
    print_status_count()
