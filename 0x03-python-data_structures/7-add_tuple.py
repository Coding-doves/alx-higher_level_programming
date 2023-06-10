#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # 1st method: using map() and lambda()

    # only first 2 tuples needed
    a = tuple_a[:2]
    b = tuple_b[:2]

    # if an element is missing, pad with zero
    a = a + (0, ) * (2 - len(a))
    b = b + (0, ) * (2 - len(b))

    for i in range(0, 2):
        tupl = tuple(map(lambda x, y: x + y, a, b))

    return(tupl)

    """
    # 2nd method: using loop

    # only first 2 tuples needed
    x = tuple_a[:2]
    y = tuple_b[:2]

    # if an element is missing, pad with zero
    x = x + (0, ) * (2 - len(x))
    y = y + (0, ) * (2 - len(y))

    tupl = []
    for i in range(0, 2):
        tupl.append(x[i] + y[i])
    res = tuple(tupl)
    return(res)
    """
