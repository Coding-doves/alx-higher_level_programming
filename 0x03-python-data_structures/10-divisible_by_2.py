#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_ls = list(my_list)

    for n in new_ls:
        if n % 2 == 0:
            return new_ls, True
        else:
            return new_ls, False
