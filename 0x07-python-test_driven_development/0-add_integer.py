#!/usr/bin/python3
"""This function perform basic maths addition

Function:
    - add_integer(a, b): Adds two number
"""


def add_integer(a, b=98):
    """Returns:
        int: result of a + b
    """
    if a is None or type(a) == str:
        raise TypeError("a must be an integer")
    elif b is None or type(b) == str:
        raise TypeError("b must be an integer")
    elif not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    elif isinstance(a, float):
        a = int(a)
    elif isinstance(b, float):
        b = int(b)
    elif a and b:
        return int(a + b)
