#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0:
        return(my_list)
    if idx > len(my_list) - 1:
        return(my_list)

    for s in range(0, len(my_list)):
        if my_list[s] == idx:
            my_list[s + 1] = element
            return(my_list)
