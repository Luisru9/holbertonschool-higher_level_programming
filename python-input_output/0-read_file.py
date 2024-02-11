#!/usr/bin/python3
"""0. Read file"""


def read_file(filename=""):
    """
    Function that reads a text file (UTF8) and prints it to stdout
    Args:
        filename: Name of the file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
