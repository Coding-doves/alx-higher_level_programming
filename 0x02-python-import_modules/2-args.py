#!/usr/bin/python3

def arg_len(*argvs):
    return(len(argvs))


if __name__ == "__main__":
    import sys

    ags = sys.argv[1:]

    if len(ags) == 1:
        print("{} argument:".format(len(ags)))
    else:
        print("{} arguments:".format(len(ags)))

    for index, a in enumerate(ags):
        print("{}: {}".format(index + 1, a))
