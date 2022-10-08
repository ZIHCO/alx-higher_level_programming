#!/usr/bin/python3
def uppercase(str):
    i = 0

    while i < len(str):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            char = ord(str[i]) - 32
        else:
            char = ord(str[i])
        print("{:c}".format(char), end='')
        i = i + 1
    print("")
