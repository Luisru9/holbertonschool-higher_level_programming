#!/usr/bin/python3

import json


def to_json_string(my_obj):
    """
    Function that returns the JSON representation of an object (string)
    Args:
        my_obj: Object to be converted to JSON
    Returns:
        JSON representation of the object
    """
    return json.dumps(my_obj)
