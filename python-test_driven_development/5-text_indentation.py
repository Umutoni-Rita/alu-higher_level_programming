#!/usr/bin/python3
"""
This module provides text_indentation, a function that prints
a text with 2 new lines after each of the characters '.', '?' and ':'.
No printed line starts or ends with a space.
"""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?' and ':'.
    Raise a TypeError if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"
    lines = [line.strip(" ") for line in result.split("\n")]
    print("\n".join(lines), end="")
