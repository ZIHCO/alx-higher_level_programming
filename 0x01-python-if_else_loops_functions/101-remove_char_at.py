#!/usr/bin/python3
def remove_char_at(str, n):
    """a function that creates a copy of the string,
    removing the character at the position n
    (not the Python way, the “C array index”).

    parameters:
    ----------
    str: a string argument
    n: integer argument, position to ommit

    Returns:
    --------
    a copy with the char at index n ommitted
    """

    i = 0
    newstr = ""

    while i < len(str):
        if i == n:
            pass
        else:
            newstr = newstr + str[i]
        i = i + 1
    return newstr
