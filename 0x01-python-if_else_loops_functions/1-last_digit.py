#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number >= 0):
    if (number % 10) > 5:
        print(f"Last digit of {number:d} is {(number % 10):d}"
              " and is greater than 5")
    elif (number % 10) <= 5 & (number % 10) > 0:
        print(f"Last digit of {number:d} is {(number % 10):d}"
              " and is less than 6 and not 0")
    elif number % 10 == 0:
        print(f"Last digit of {number:d} is {(number % 10):d} and is 0")
else:
    if (-1 * number) % 10 > 5:
        print(f"Last digit of {number:d} is {((-1 * number) % 10) * (-1):d}"
              " and is greater than 5")
    elif (-1 * number) % 10 <= 5 & (-1 * number) % 10 > 0:
        print(f"Last digit of {number:d} is {((-1 * number) % 10) * (-1):d}"
              " and is less than 6 and not 0")
    elif (-1 * number) % 10 == 0:
        print(f"Last digit of {number:d} is {((-1 * number) % 10):d} and is 0")
