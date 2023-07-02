#!/usr/bin/python3
"""Function prints square shape made with #"""


def print_square(size):
    """Parameter:
        size(int): size to square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        size = int(size)
        for i in range(size):
            print("#" * size)
