#!/usr/bin/python3
class Square:
    """Creating a square shape.

    Attributes:
        size (int): size of the square length

    """
    def __init__(self, size=0):
        """Initialize a Square instance.

         Args:
            size(int, optional): size of square length

        Raises:
             TypeError: if size is not an integer
             ValueError: If size is less than zero

         """
        self.size = size

    @property
    def size(self):
        """get the property size/to retrieve it

         Returns:
            int: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """to set it"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the area of the square

        Returns:
            int: current square area

        """
        return int(self.size) ** 2
