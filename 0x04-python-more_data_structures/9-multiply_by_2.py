#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}

    for key, val in dict.items(a_dictionary):
        val *= 2
        new_dict[key] = val
    return new_dict
