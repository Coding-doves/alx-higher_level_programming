#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    leng = len(sys.argv)
    args = sys.argv
    operator = ["+", "-", "*", "/"]

    if leng - 1 != 3:
        print("Usage: {} <a> <operator> <b>".format(args[0]))
        sys.exit(1)
    if args[2] not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    for i in range(1, leng):
        if args[2] == operator[0]:
            total = add(int(args[1]), int(args[3]))
        if args[2] == operator[1]:
            total = sub(int(args[1]), int(args[3]))
        if args[2] == operator[2]:
            total = mul(int(args[1]), int(args[3]))
        if args[2] == operator[3]:
            total = div(int(args[1]), int(args[3]))
    print("{} {} {} = {}".format(args[1], args[2], args[3], total))
