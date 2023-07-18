#!/usr/bin/python3
'''square model'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    initialization
    atrributes for our square, having them inherit
    from Rectangle
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''initialization'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''getters'''
        return self.width

    @size.setter
    def size(self, val):
        '''setters'''
        self.width = val
        self.height = val

    def __str__(self):
        '''string method'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        '''update of argument and key/vaule pairs'''
        num_arg = ['id', 'size', 'x', 'y']

        if args:
            for i, str_a in enumerate(args):
                if i < len(num_arg):
                    setattr(self, num_arg[i], str_a)
        elif kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        '''dictionary representation'''
        key = ['id', 'size', 'x', 'y']
        dic = {}

        for i in key:
            if i == 'size':
                dic[i] = getattr(self, 'width')
            else:
                dic[i] = getattr(self, i)

        return dic
