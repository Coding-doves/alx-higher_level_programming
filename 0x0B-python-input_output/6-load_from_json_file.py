#!/usr/bin/python3
'''import module'''

import json
'''creates an Object from a “JSON file'''


def load_from_json_file(filename):
    '''using load - reads the file and creates a dict...'''
    with open(filename) as f:
        return json.load(f)
