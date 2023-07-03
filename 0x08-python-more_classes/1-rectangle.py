#!/usr/bin/python3
'''creating prototype for a rectangle'''


class Rectangle:
    '''initializing a regtangle'''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    '''attribute:
        width(int): width of rectangle
        height(int): heightof rectangle
    '''
    @property
    def width(self):
        return self.__width

    '''setting width'''
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    '''setting height'''
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
