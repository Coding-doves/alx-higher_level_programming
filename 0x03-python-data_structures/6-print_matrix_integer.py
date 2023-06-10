#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for col_m in matrix:
        for row_m in col_m:
            print("{:d}".format(row_m), end=" ")
        print()
    """
    # 2nd code style. both are perfect
    col_m = matrix

    for i in col_m:
        for j in i:
            print("{}".format(j), end = " ")
        print()
    """
