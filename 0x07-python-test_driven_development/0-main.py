#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(6, 4))
print(add_integer(6.4, 4))
print(add_integer(-4))
print(add_integer(9, -2))
print(add_integer(6, 'a'))
print(add_integer(None))
