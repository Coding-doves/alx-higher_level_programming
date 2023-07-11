#!/usr/bin/python3
'''append string to file'''


def append_write(filename="", text=""):
    '''`a` mode'''
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
