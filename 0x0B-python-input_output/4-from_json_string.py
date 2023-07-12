#!/usr/bin/python3
'''import module'''

import json
''' returns an object (Python data structure) represented by a JSON string'''


def from_json_string(my_str):
    '''using json.load'''
    return json.loads(my_str)
