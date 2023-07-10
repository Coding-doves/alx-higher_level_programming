#!/usr/bin/python3
'''checking if the object is exactly an instance of the specified class '''


def is_same_class(obj, a_class):
    '''checking for instance'''
    if type(obj) is a_class:
        return True
    else:
        return False
