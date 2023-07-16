#!/usr/bin/python3
from models.rectangle import Rectangle


if __name__ == '__main__':
    r1 = Rectangle(10, 2)
    print(r1.height)

    r2 = Rectangle(2, 10)
    print(r2.height)

    r1 = Rectangle(3, 2)
    print(r1.area())

    r2 = Rectangle(2, 10)
    print(r2.area())

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())
