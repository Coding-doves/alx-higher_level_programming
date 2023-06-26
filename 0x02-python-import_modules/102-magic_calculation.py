#!/usr/bin/python3
import dis
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    if(a < b):
        c = add(a, b)
        for i in range(4, 7):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
    """
    bytcode = dis.Bytecode(magic_calculation)
    for instr in bytcod:
        print(instr)
    """
