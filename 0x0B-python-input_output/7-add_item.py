#!/usr/bin/python3
'''import module'''


import sys
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
file = "add_item.json"
list_store = []

'''using json.load'''
if exists(file):
    list_store = load_from_json_file(file)

list_store.extend(args[1:])
save_to_json_file(list_store, file)
