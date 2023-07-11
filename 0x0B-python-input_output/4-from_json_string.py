#!/usr/bin/python3
'''import module'''

import json
''' returns an object (Python data structure) represented by a JSON string'''


def from_json_string(my_str):
    return json.dumps(my_str)
