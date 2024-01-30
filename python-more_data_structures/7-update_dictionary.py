#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Use dictionary unpacking to replace or add key-value pairs
    a_dictionary = {**a_dictionary, key: value}
