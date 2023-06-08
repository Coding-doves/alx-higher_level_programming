#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    a = int(sys.argv[1:])
    size = len(a)
    plus = 0

    for i, b in enumerate(a):
        plus = plus + a
        print("{}".format(plus))
