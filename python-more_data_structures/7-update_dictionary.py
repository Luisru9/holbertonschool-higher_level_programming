#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Use dictionary unpacking to replace or add key-value pairs
    a_dictionary = {**a_dictionary, key: value}


# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3}
update_dictionary(my_dict, 'b', 4)  # Update existing key 'b'
update_dictionary(my_dict, 'd', 5)  # Add new key 'd'
update_dictionary(my_dict, 'a', 10)  # Update existing key 'a'
