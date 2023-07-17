#!/usr/bin/python3
'''square model'''


from models.rectangle import Rectangle

class Square(Rectangle):
    '''initialization'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    '''getters'''
    @property
    def size(self):
        return self.width

    '''setters'''
    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    '''string method'''
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    '''==================update of argument and key/vaule pairs==========='''
    def update(self, *args, **kwargs):
        num_arg = ['id', 'size', 'x', 'y']

        if args:
            for i, a in enumerate(args):
                if i < len(num_arg):
                    setattr(self, num_arg[i], a)
        elif kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)

    '''==================dictionary representation==========='''
    def to_dictionary(self):
        key = ['id', 'size', 'x', 'y']
        dic = {}

        for i in key:
            if i == 'size':
                dic[i] = getattr(self, 'width')
            else:
                dic[i] = getattr(self, i) 

        return dic
