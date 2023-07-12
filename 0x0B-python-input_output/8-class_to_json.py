#!usr/bin/python3
'''JSON serialization'''


def class_to_json(obj):
    '''using json.dumps'''
    return obj.__dict__
