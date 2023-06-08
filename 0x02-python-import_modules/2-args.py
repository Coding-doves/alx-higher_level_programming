#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    num = len(sys.argv) - 1

    if num == 1:
        print("{} argument:".format(num))
    elif num == 0:
        print("{} arguments:".format(num))
    else:
        print("{} arguments:".format(num))

    for i, a in enumerate(sys.argv[1:]):
        print("{}: {}".format(i + 1, a))
