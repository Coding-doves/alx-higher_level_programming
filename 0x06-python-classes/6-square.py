#!/usr/bin/python3
"""Creating class object Square"""


class Square:
    """Creating a square shape.

    Attributes:
        size (int): size of the square length

    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square instance.

         Args:
            size(int, optional): size of square length

        Raises:
             TypeError: if size is not an integer
             ValueError: If size is less than zero

         """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """to retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """to set position"""
        if type(value) is tuple and len(value) == 2:
            for p in value:
                if p < 0:
                    raise TypeError
                    print("position must be a tuple of 2 positive integers")
            self.__position = value
        else:
            raise TypeError
            print("position must be a tuple of 2 positive integers")

    def area(self):
        """Calculates the area of the square

        Returns:
            int: current square area

        """
        return int(self.size) ** 2

    def my_print(self):
        """that prints in stdout the square with the character #

        and prints first, the position - this represents the 
        horizontal/row(position[0])/right and vertical/column(position[1])/down
        offset of the square's top-left corner. It determines where the square
        will be printed in relation to the left and top edges of the output.

        """

        if self.size > 0:
            """loop to set position"""
            for j in range(self.position[1]):
                if self.position[1] > 0:
                    print()

            """loop to create square #"""
            for i in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
        elif self.size == 0:
            print()
