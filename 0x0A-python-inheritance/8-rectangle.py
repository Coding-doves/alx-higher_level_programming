#!/usr/bin/python3
'''creating base geometry class'''


class BaseGeometry:
    '''handle exception'''
    def area(self):
        raise Exception('area() is not implemented')

    '''that validates value'''
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


''' creating a class Rectangle that inherits from BaseGeometry'''


class Rectangle(BaseGeometry):
    '''initializing width and height'''
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        if height <= 0 and type(height) != int and\
                isinstance(height, (str, float)):
            raise TypeError('{} must be an integer'.format(height))
        if width <= 0 and type(width) is not int:
            raise TypeError('{} must be an integer'.format(width))
