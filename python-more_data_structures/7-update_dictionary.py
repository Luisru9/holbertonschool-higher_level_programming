#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Use the setdefault method to replace or add key-value pairs
    a_dictionary.setdefault(key, value)
    return a_dictionary
