#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        # Attempting to use an undefined variable to raise a NameError
        undefined_variable
    except NameError:
        # Raising a custom NameError with the provided message
        raise NameError(message)
