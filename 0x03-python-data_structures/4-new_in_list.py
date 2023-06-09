#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    if idx < 0:
        return(my_list)
    if idx > len(my_list) - 1:
        return(my_list)

    new_ls = list(my_list)
    for i in range(len(new_ls)):
        if new_ls[i] == idx:
            new_ls[idx] = element
    return(new_ls)
