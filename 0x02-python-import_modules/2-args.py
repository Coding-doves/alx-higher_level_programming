#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    ags = sys.argv[1:] 
    num = len(ags)

    if len(ags) == 1:
        print("{} argument:".format(num))
    else:
        print("{} arguments:".format(num))

    for i, a in enumerate(ags):
        print("{}: {}".format(i + 1, a))
