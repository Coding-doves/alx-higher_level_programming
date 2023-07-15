#!/usr/bin/python3
'''base class for this project'''


class Base:
    '''private class attribute'''
    __nb_objects = 0

    '''initializing base'''
    def __init__(self, id=None):
        if id is None:
            '''if id is not given'''
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        if id is not None:
            self.id = id
