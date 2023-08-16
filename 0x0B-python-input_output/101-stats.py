#!/usr/bin/python3
"""This module is a script for getting HTTP responses"""


if __name__ == "__main__":
    from sys import stdin

    line = stdin.readline()
    while line != "":
        result_dict = {"File size": 0, "200": 0, "301": 0, "400": 0, "401": 0,
                       "403": 0, "404": 0, "405": 0, "500": 0}
        for i in range(10):
            make_list = line.split()
            result_dict["File size"] += int(make_list[-1])
            result_dict[(make_list[-2])] += 1
            line = stdin.readline()
        code_list = list((result_dict))
        for item in code_list:
            if result_dict[item] > 0:
                print(f"{item}: {result_dict[item]}")
