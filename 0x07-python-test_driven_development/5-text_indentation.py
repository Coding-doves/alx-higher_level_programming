#!/usr/bin/python3
"""Function prints text"""


def text_indentation(text):
    """Text is a str and must create 2 new line
    if it encounters `.` `?` `:`
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    elif text == "" or text == " ":
        return
    else:
        text = text.strip()
        for i in text:
            print(i, end='')
            if i == '.' or i == '?' or i == ':':
               print('\n')
