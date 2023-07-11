#!/usr/bin/python3
''' function that reads a text file (UTF8) and prints it to stdout'''


def read_file(filename=""):
    ''' the use of with and utf-8'''
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end='')
