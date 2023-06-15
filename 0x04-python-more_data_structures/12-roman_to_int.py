#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_num = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    add = 0
    length = len(roman_string)

    for i in range(length):
        if i < l - 1 and rom_num[roman_string[i]]"/"
        < rom_num[roman_string[i + 1]]:
            add -= rom_num[roman_string[i]]
        else:
            add += rom_num[roman_string[i]]
    return add
