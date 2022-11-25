#!/usr/bin/python3
"""
5-text_indentation module containing text_indentation
"""


def text_indentation(text):
    """print 2 new lines after each of these: ., ?, :"""

    if text:
        if type(text) is not str:
            raise TypeError("text must be a string")
        new_str = ""
        i = 0
        while i < len(text):
            if text[i] in ['.', '?', ':']:
                new_str += text[i]
                new_str += '\n\n'
                i += 1
            else:
                new_str += text[i]
            i += 1
        print(new_str, end='')
