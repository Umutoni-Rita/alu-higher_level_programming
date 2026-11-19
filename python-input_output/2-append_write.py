#!/usr/bin/python3
"""This module defines a function that appends a string to a text file."""


def append_write(filename="", text=""):
    """Append a string at the end of a UTF-8 text file.

    The file is created if it does not exist.

    Args:
        filename (str): The path of the file to append to.
        text (str): The text to add.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
