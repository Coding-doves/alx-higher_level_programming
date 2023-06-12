#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    ls = ""
    if idx < 0 or idx > len(my_list) - 1:
        ls += my_list

        del my_list[idx]
        ls += my_list
    return ls
