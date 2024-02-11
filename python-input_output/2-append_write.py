#!/usr/bin/python3
"""2. Appended file"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text file (UTF8) and returns the number of characters added
    Args:
        filename: Name of the file
        text: Text to append to the file
    Returns:
        The number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        num_chars_added = f.write(text)
    return num_chars_added
