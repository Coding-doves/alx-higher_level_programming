#!/usr/bin/python3
'''creating base geometry class'''


class BaseGeometry:
    '''handle exception'''
    def area(self):
        raise Exception('area() is not implemented')
