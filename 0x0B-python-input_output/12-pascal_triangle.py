#!/usr/bin/python3
'''pascal_triangle'''


def pascal_triangle(n):
    list_t = []

    if n <= 0:
        return []

    for i in range(1, n):
        list_t.append([])
        for j in range(1, i):
            list_t.append([j])

