#!/usr/bin/python3
class Square:
    """creating a square shape.

    Attributes:
        size (int): size of the square length

    """
    def __init__(self, size=0):
        """Initialize a Square instance.

         Args:
            size(int): size of square length

        Raises:
             TypeError: if size is not an integer
             ValueError: If size is less than zero

         """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculates the area of the square

        Returns:
            int: current square area

        """
        return self.__size ** 2
