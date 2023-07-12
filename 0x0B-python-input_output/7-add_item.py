#!/usr/bin/python3
'''import module'''


import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
file = "add_item.json"

'''using json.load'''
if (file):
    list_store = load_from_json_file(file)

list_store = []
list_store.extend(args[1:])
save_to_json_file(list_store, file)
