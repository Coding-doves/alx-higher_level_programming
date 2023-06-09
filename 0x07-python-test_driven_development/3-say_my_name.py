#!/usr/bin/python3
"""function prints fullname

Name must be in str. No other type is allowed
"""


def say_my_name(first_name, last_name=""):
    """Parameters:
        first_name(str): print first name
        last_name(str): print last name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
