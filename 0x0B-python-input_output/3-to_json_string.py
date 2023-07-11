#!/usr/bin/python3
'''import module'''

import json
''' returns an object (Python data structure) represented by a JSON string'''


def to_json_string(my_str):
    '''function to handle task'''
    return json.dumps(my_str)
