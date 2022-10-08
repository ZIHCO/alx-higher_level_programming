#!/usr/bin/python3
def main():
    for i in range(122, 96, -2):
        print("{:c}{:c}".format(i, (i - 33)), end="")


main()
