#!/usr/bin/python3
'''data of student'''


class Student:
    '''initializing needed data'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    '''attribute list retrieve'''
    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            dict_store = {}

            for i in attrs:
                if i in self.__dict__:
                    dict_store[i] = self.__dict__[i]

        return dict_store

    ''' that replaces all attributes of the Student instance'''
    def reload_from_json(self, json):
        self.__dict__.update(json)
