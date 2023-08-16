#!/usr/bin/python3
"""This script reads from stdin"""

from sys import stdin

line = stdin.readline()
i = 0
line_dict = {"File size": 0, "200": 0, "301": 0, "400": 0, "401": 0,
             "403": 0, "404": 0, "405": 0, "500": 0}
try:
    while line:
        if i % 10 == 0 and i != 0:
            print(f"File size: {line_dict['File size']}")
            list_code = list(sorted(line_dict))[:-1]
            for item in list_code:
                if line_dict[item] != 0:
                    print(f"{item}: {line_dict[item]}")
            i = 0
            continue
        line_list = line.split()
        line_dict['File size'] += int(line_list[-1])
        line_dict[line_list[-2]] += 1
        line = stdin.readline()
        i += 1
except KeyboardInterrupt:
    print(f"File size: {line_dict['File size']}")
    list_code = list(sorted(line_dict))[:-1]
    for item in list_code:
        if line_dict[item] != 0:
            print(f"{item}: {line_dict[item]}")
    raise
