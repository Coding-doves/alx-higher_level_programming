#!/usr/bin/python3
"""This function perform basic maths addition

Function:
    - add_integer(a, b): Adds two number
"""


def add_integer(a, b=98):
    """Returns:
        int: result of a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    elif isinstance(a, float):
        a = int(a)
    elif isinstance(b, float):
        b = int(b)

    return int(a + b)
