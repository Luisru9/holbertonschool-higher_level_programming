#!/usr/bin/python3
def raise_exception():
    try:
        # Attempting an operation that would cause a TypeError
        result = 1 + "2"
    except TypeError as e:
        # Raising a custom type exception with a specific message
        raise TypeError("Custom type exception: {}".format(e))
