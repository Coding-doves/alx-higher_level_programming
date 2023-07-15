#!/usr/bin/python3
'''prototype rectangle'''


from models.base import Base

class Rectangle(Base):
    '''nitializing rectangle'''
    def __init__(self, width=0, height=0, x=0,  y=0, id=None):
        '''super module use in call the base class once'''
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    '''getters'''
    @property
    def width(self):
        return self.__width

    '''setter'''
    @width.setter
    def width(self, val):
        if type(val) is not int:
            raise TypeError("width must be an integer")
        elif val <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = val

    '''getters'''
    @property
    def height(self):
        return self.__height

    '''setter'''
    @height.setter
    def height(self, val):
        if type(val) is not int:
            raise TypeError("height must be an integer")
        elif val <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = val

    '''getters'''
    @property
    def x(self):
        return self.__x

    '''setter'''
    @x.setter
    def x(self, val):
        if type(val) is not int:
            raise TypeError("x must be an integer")
        elif val < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = val

    '''getters'''
    @property
    def y(self):
        return self.__y

    '''setter'''
    @y.setter
    def y(self, val):
        if type(val) is not int:
            raise TypeError("y must be an integer")
        elif val < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = val

    '''area of rectangle'''
    def area(self):
        return self.__width * self.__height
    
    '''display "#" of rectangle'''
    def display(self):
        if self.__width == 0:
            return ''
        else:
            for i in range(self.__y):
                if i > 0:
                    print()

            return '\n'.join(str(" ") * self__x + str('#') * self.__width for i in range(height))

    '''magic method'''
    def __str__(self):
        return "f{'[Rectangle]' (self.id()) self.x()/self.y() - self.width()/height()}"

    '''update class'''
    def update(self, *args, **kwargs):
        num_args = len(args)

        if num_args >= 1:
            self.id = args[0]
        elif num_args >= 2:
            self.__width = args[2]
        elif num_args >= 3:
            self.__height = args[3]
        elif num_args >= 4:
            self.__x = args[4]
        elif num_args >= 5:
            self.__y = args[5]
