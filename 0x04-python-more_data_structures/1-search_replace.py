#!/usr/bin/python3
def search_replace(my_list, search, replace):
    s = []
    for lit in my_list:
        if lit == search:
            s.append(replace)
        else:
            s.append(lit)
    return s
