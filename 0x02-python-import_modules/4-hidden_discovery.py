#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    fp = dir(hidden_4)

    for i in fp:
        if i[0:2] != '__':
            print("{:s}".format(i))
