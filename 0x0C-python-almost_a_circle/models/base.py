#!/usr/bin/python3
'''base class for this project'''
import json


class Base:
    '''private class attribute'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''initializing base'''
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        if id is not None:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation of list_dictionaries'''
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file'''
        file = cls.__name__ + '.json'
        cpy_list = []

        if list_objs is not None:
            for i in list_objs:
                cpy_list.append(i.to_dictionary())

        with open(file, 'w', encoding='utf-8') as file_name:
            file_name.write(cls.to_json_string(cpy_list))

    @staticmethod
    def from_json_string(json_string):
        '''returns the list of the JSON string representation'''
        if json_string is None:
            return '[]'
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''creating a dummy instance value'''
        if cls.__name__ == "Rectangle":
            dum = cls(1, 1)
        elif cls.__name__ == "Square":
            dum = cls(1)
        else:
            dum = cls()

        dum.update(**dictionary)

        return dum

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances'''
        file = cls.__name__ + '.json'
        init_list = []

        if file:
            with open(file, 'r', encoding='utf-8') as file_name:
                store = file_name.read()

                stored_json_str = cls.from_json_string(store)

                for j in stored_json_str:
                    init_list.append(cls.create(**j))

                return init_list
        else:
            return init_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''convert list to key/value pair and save in a file'''
        file = cls.__name__ + '.csv'
        objs = []

        if list_objs is not None:
            for i in list_objs:
                objs.append(i.to_dictionary())

        with open(file, 'w', encoding='utf-8') as file_name:
            file_name.write(cls.to_json_string(objs))

    def load_from_file_csv(cls):
        '''returns a list of instances in csv format'''
        file = cls.__name__ + '.csv'
        str_to_read = []

        if file is not None:
            with open(file, 'r', encoding='utf-8') as file_name:
                byts = file_name.read()
                store = cls.from_json_string(byts)

                for j in store:
                    str_to_read.append(cls.create(**j))

                return str_to_read
        else:
            return str_to_read
