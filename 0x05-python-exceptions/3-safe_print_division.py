#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        if a == 0 or b == 0:
            result = None
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
    return result
