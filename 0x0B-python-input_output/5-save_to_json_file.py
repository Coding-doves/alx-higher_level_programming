#!/usr/bin/python3
'''import module'''

import json
'''writes an Object to a text file, using a JSON representation'''


def save_to_json_file(my_obj, filename):
    '''using json.dumps'''
    with open(filename, 'w') as f:
        return json.dump(my_obj, f)
