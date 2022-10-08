#!/usr/bin/python3
def print_last_digit(number):
    cpynum = number
    if cpynum < 0:
        cpynum = (-1) * number
        if cpynum < 0:
            cpynum = -cpynum
    print("{:d}".format(cpynum % 10), end="")
    return cpynum % 10
