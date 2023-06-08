#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    index = len(sys.argv)
    plus = 0

    for i in range(1, index):
        plus = plus + int(sys.argv[i])
    print("{}".format(plus))
