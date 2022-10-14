#!/usr/bin/python3
"""
    imports all the functions from the module
    calculator_1.py
    arguments:
    commandline argument
    a: integer
    b: integer
    operator: arithmetic opertors
"""
from calculator_1 import add, sub, mul, div
import sys
import builtins

argc = len(sys.argv)
if argc != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

num1 = int(sys.argv[1])
num2 = int(sys.argv[3])
if __name__ == "__main__":
    if sys.argv[2] == '+':
        print("{:d} + {:d} = {:d}".format(num1, num2, add(num1, num2)))
    elif sys.argv[2] == '-':
        print("{:d} - {:d} = {:d}".format(num1, num2, sub(num1, num2)))
    elif sys.argv[2] == '*':
        print("{:d} * {:d} = {:d}".format(num1, num2, mul(num1, num2)))
    elif sys.argv[2] == '/':
        print("{:d} / {:d} = {:d}".format(num1, num2, div(num1, num2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
