#!/usr/bin/python3
'''prototype rectangle'''

from models.base import Base


class Rectangle(Base):
    '''
    initializing rectangle
    '''
    def __init__(self, width=0, height=0, x=0,  y=0, id=None):
        '''super module use in call the base class once'''
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''getters'''
        return self.__width

    @width.setter
    def width(self, val):
        '''setter'''
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")

        self.__width = val

    @property
    def height(self):
        '''getters'''
        return self.__height

    @height.setter
    def height(self, val):
        '''setter'''
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")

        self.__height = val

    @property
    def x(self):
        '''getters'''
        return self.__x

    @x.setter
    def x(self, val):
        '''setter'''
        if not isinstance(val, int):
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")

        self.__x = val

    @property
    def y(self):
        '''getters'''
        return self.__y

    @y.setter
    def y(self, val):
        '''setter'''
        if not isinstance(val, int):
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")

        self.__y = val

    def area(self):
        '''
        Gets the area of the rectangle
        Attributes:
        self.__width(int)
        self.__height(int)
        '''
        return self.__width * self.__height

    def display(self):
        '''display "#" of rectangle'''
        if self.__width == 0:
            print()
        else:
            for i in range(self.__y):
                if i >= 0:
                    print()

            print('\n'.join(
                str(" ") * self.__x + str('#') * self.__width
                for i in range(self.__height)))

    def __str__(self):
        '''magic method'''
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        '''update class Rectangle public __init__ attribute'''
        if args:
            num_args = ['id', 'width', 'height', 'x', 'y']

            for i, string in enumerate(args):
                if i < len(num_args):
                    setattr(self, num_args[i], string)
        elif kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        '''dictionary representation'''
        keys = ['id', 'width', 'height', 'x', 'y']
        dic = {}

        for i in keys:
            dic[i] = getattr(self, i)

        return dic
