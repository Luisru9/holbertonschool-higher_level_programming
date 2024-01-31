#!/usr/bin/python3
def raise_exception():
    try:
        # Raise a custom type exception
        raise TypeError(
            "Custom type exception: This is an intentional exception.")
    except TypeError as e:
        # Print the exception message
        print(e)
