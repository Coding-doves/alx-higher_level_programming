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
            print()
        else:
            for i in range(self.__y):
                if i >= 0:
                    print()

            print('\n'.join(str(" ") * self.__x + str('#') * self.__width for i in range(self.__height)))

    '''magic method'''
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    '''update class Rectangle public __init__ attribute'''
    def update(self, *args, **kwargs):
        if args:
            num_args = ['id', 'width', 'height', 'x', 'y']

            for i, s in enumerate(args):
                if i < len(num_args):
                    setattr(self, num_args[i], s)
        elif kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)
