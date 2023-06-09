#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    rev = []
    for i in range(len(my_list) - 1, -1, -1):
        rev = my_list[i]
        print("{}".format(rev), sep='\n')
