#!/usr/bin/python3

def uppercase(str):
    z = ""

    for s in str:
        if ord(s) >= 97 and ord(s) <= 122:
            x = ord(s) - 32
            y = chr(x)
            z += y
        else:
            z += s

    print("{}".format(z), end="")
    print()
