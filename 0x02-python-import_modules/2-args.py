#!/usr/bin/python3
import sys
if __name__ == "__main__":
    """prints the number of and the list of its arguments.
    Takes commandline argument.
    """
    argc = len(sys.argv)
    if (argc == 2):
        print("1 argument:\n{:d}: {:s}".format((argc - 1), sys.argv[1]))
    elif (argc > 2):
        print("{:d} arguments:".format(argc - 1))
        for i in range(1, argc):
            print("{:d}: {:s}".format(i, sys.argv[i]))
    else:
        print("0 arguments.")
