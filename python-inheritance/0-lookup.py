#!/usr/bin/python3
"""Lookup
Returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    Args:
        obj: object to look up
    Returns:
        list of available attributes and methods
    """
    return dir(obj)
