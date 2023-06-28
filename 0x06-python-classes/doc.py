#!/usr/bin/python3
def has_documentation(obj):
    return obj.__doc__ is not None

# Example usage:
print(has_documentation(Square))    # Check if class has documentation
