#!/usr/bin/python3
"""
This module provides a function that prints text with two new lines after
each '.', '?', and ':'.

The function text_indentation ensures the input is a string and formats the
text accordingly.
"""


def text_indentation(text):
    """
    Prints text with two new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = ['.', '?', ':']
    start = 0
    for idx, char in enumerate(text):
        if char in delimiters:
            print(text[start:idx + 1].strip() + "\n")
            start = idx + 1
    if start < len(text):
        print(text[start:].strip(), end="")
