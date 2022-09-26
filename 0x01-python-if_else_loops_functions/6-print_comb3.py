#!/usr/bin/python3
for i in range(0, 9):
    for j in range(0, 10):
        if i != j:
            if i < j:
                if i != 8:
                    print("{:d}".format(i), end='')
                    print("{:d}".format(j), end=', ')
                else:
                    print("{0:d}{1:d}".format(i, j))
