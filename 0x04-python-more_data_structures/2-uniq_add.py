#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = set(my_list)
    add = 0
    for i in s:
        add += i
    return add
