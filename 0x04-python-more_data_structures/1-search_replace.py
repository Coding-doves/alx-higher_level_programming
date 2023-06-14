#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i, lit in enumerate(my_list):
        if lit == search:
            my_list[i] = replace
    return my_list
