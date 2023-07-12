#!/usr/bin/python3
'''import module'''


import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
file = "add_item.json"

with open(file, 'a+', encoding="utf-8") as f:
    '''using json.load'''
    list_store = []
    list_store.extend(args[1:])
    save_to_json_file(list_store, file)
    load_from_json_file(file)
