#!/usr/bin/python3
def print_last_digit(number):
    cpynum = number
    if cpynum < 0:
        cpynum = (-1) * number
        if cpynum < 0:
            cpynum = -cpynum
    return cpynum % 10
