#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    Function that writes a string to a text file (UTF8) and returns the number of characters written
    Args:
        filename: Name of the file
        text: Text to write to the file
    Returns:
        The number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        num_chars_written = f.write(text)
    return num_chars_written
