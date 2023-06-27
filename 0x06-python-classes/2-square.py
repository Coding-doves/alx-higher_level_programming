#!/usr/bin/python3
class Square:
    """Creating a square shape.

    Attributes:
        size (int): size of the square length

    """

    def __init__(self, size=0):
        """Initialize a Square instance.

         Args:
            size (int): size of square length

         Raises:
             TypeError: if size is not an integer
             ValueError: If size is less than zero

         """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= :x
