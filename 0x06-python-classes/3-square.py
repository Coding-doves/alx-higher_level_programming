#!/usr/bin/python3
class Square:
    """creating a class object called square"""
    def __init__(self, size=0):
        """the __init__ method itself

         Args:
            size(int): size of `Square`
            area(int): area of `Square`

        Raises:
             TypeError: if `size` is not an integer
             ValueError: If `size` is less than zero

         """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        def area(self):
            """this is a Class method

            Returns:
                the current square area

            """
            return self.__size ** 2
