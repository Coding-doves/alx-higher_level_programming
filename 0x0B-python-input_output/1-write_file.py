#!/usr/bin/python3
'''function that writes a string to stdout'''


def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
