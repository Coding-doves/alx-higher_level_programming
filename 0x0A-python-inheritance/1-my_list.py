#!/usr/bin/python3
'''inherits from a list'''


class MyList(list):
    '''prints list, sorted (ascending sort)'''
    def print_sorted(self):
        '''prints list'''
        s = list.sort(self)
        return s
