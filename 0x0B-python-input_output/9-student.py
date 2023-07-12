#!/uer/bin/python3
'''data of student'''

import json


class Student:
    '''initializing needed data'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return json.dumps(self.__dict__)