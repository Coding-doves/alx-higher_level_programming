#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j = 0
    for i in range(x):
        try:
            int(my_list[i])
            if False:
                continue
            print("{:d}".format(my_list[i]), end="")
            j += 1
        except TypeError:
            pass
        except ValueError:
            pass
    print()
    return j
