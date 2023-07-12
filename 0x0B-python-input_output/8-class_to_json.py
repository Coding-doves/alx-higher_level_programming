#!/usr/bin/python3
'''import module'''


import json
'''JSON serialization of an object'''


def class_to_json(obj):
    '''using json.dumps'''
    return obj.__dict__
