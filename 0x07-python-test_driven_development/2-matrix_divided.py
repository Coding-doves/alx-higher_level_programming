#!/usr/bin/python3
"""Function divides matrix by a given number

Returns:
    a divided matrix
"""


def matrix_divided(matrix, div):
    """Parameters:
        matrix(int): numbers to div
        div(int): const for div matrix
    """

    s = []
    r = []
    for i in matrix:
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError("matrix must be a matrix (list of lists) \
                        of integers/floats")
            elif len(matrix[0]) < len(matrix[1]) or \
                    len(matrix[0]) > len(matrix[1]):
                raise TypeError("Each row of the matrix must have the \
                        same size")
            elif not isinstance(div, int) and not isinstance(div, float):
                raise TypeError("div must be a number")
            elif div == 0:
                raise ZeroDivisionError("division by zero")
            else:
                j = round(j / div, 2)
            r.append(j)
        s.append(list(r))
        r = []
    return s
