#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    if idx < 0 or idx >= len(my_list):
        return(my_list)
    else:
        new_ls = list(my_list)
        new_ls[idx] = element
        return(new_ls)
