#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    res = 0
    try:
        for i in range(list_length):
            try:
                if isinstance(my_list_1[i], str) or\
                        isinstance(my_list_2[i], str):
                    res = 0
                    print("wrong type")
                elif my_list_2[i] == 0:
                    res = 0
                    print("division by 0")
                else:
                    res = my_list_1[i] / my_list_2[i]

            except IndexError:
                res = 0
                print("out of range")
            except TypeError:
                pass
            except ZeroDivisionError:
                pass
            result.append(res)
    finally:
        return result
