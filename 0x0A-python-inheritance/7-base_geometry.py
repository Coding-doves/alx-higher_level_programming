#!/usr/bin/python3
'''creating base geometry class'''


class BaseGeometry:
    '''handle exception'''
    def area(self):
        raise Exception('area() is not implemented')

    '''that validates value'''
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
