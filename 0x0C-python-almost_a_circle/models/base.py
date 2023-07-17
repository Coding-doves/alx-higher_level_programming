#!/usr/bin/python3
'''base class for this project'''


import json
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

    '''static method to'''
    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation of list_dictionaries'''
        if list_dictionaries == None:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    '''classs method save'''
    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file'''
        file = cls.__name__ + '.json'
        cpy_list = []

        if list_objs is not None:
            for i in list_objs:
                cpy_list.append(i.to_dictionary())

        with open(file, 'w') as f:
            f.write(cls.to_json_string(cpy_list))

    '''static method from'''
    @staticmethod
    def from_json_string(json_string):
        '''returns the list of the JSON string representation'''
        if json_string == None:
            return '[]'
        else:
            return json.loads(json_string)

    '''class method create'''
    @classmethod
    def create(cls, **dictionary):
        '''creating a dummy instance value'''
        if cls.__name__ == "Rectangle":
            dum = cls(1, 1, 0, 0, 1)
        elif cls.__name__ == "Square":
            dum = cls(1, 0, 0, 1)
        else:
            dum = cls()

        '''update our dummy instance value to 
        current/given vaule
        '''
        dum.update(**dictionary)

        return dum

    '''class method load'''
    @classmethod
    def load_from_file(cls):
        '''returns a list of instances'''
        file = cls.__name__ + '.json'
        init_list = []

        if file:
            '''open the file in read mode => store byte in variable `store`'''
            with open(file, 'r') as f:
                store = f.read()

                ''' pass read bytes to get json str represention'''
                stored_json_str = cls.from_json_string(store)

                '''loop through each key/value pair
                pass it to create() and append result to init_list'''
                for j in stored_json_str:
                    init_list.append(cls.create(**j))

                return init_list
        else:
            return init_list

    '''========== handle csv  serialize and deserialize ========'''
    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''convert list to key/value pair and save in a file'''
        file = cls.__name__ + '.csv'
        objs = []

        if list_objs is not None:
            for i in list_objs:
                objs.append(i.to_dictionary())

        with open(file, 'w') as f:
            f.write(cls.to_json_string(objs))

    '''load json str'''
    def load_from_file_csv(cls):
        '''returns a list of instances in csv format'''
        file = cls.__name__ + '.csv'
        s = []

        if file is not None:
            with open(file, 'r') as f:
                byts = f.read()
                store = cls.from_json_string(byts)

                for j in store:
                    s.append(cls.create(**j))

                return s
        else:
            return s
