#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_ls = []

    for n in my_list:
        if n % 2 == 0:
            new_ls.append(True)
        else:
            new_ls.append(False)
    return new_ls
