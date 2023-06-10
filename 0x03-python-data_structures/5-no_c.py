#!/usr/bin/env python3
def no_c(my_string):
    new = ""
    for s in my_string:
        if s != 'c' and s != 'C':
            new = new + s
    return(new)
