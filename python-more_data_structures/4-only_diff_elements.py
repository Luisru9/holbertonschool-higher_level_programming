#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Find elements present in only one set using set operations
    only_diff_set = (set_1 - set_2) | (set_2 - set_1)
    return only_diff_set
