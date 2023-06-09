#!/usr/bin/python3
'''creating a locked class that prevents the user from dynamically
creating new instance attributes, except if the new instance
attribute is called first_name'''


class LockedClass(object):
    '''slots holds the list of instances to be created
    preventing the any other'''
    __slots__ = ['first_name']

    def __init__(self, first_name=''):
        self.first_name = first_name
