#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for col_m in matrix:
        for row_m in col_m[:-1]:
            print("{:d}".format(row_m), end=" ")
        if len(col_m) > 0:
            print("{:d}".format(col_m[-1]))
        else:
            print()
    """
    # 2nd code style. both are perfect
    col_m = matrix

    for i in col_m:
        for j in i:
            print("{:d}".format(j), end = " ")
        print()
    """
