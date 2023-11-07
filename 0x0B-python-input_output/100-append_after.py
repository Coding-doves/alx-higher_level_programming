#!/usr/bin/python3
''' inserts a line of text to a file, after each line 
containing a specific string
'''


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'a+', encoding='utf-8') as f:
        ls = f.readlines()
        for i, s in enumerate(ls):
            if search_string in s:
                ls.insert(i + 1, new_string)

        f.writelines(new_list)

