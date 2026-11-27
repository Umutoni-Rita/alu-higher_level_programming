#!/usr/bin/python3
"""This module defines a function that writes a string to a text file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file, replacing any old content.

    The file is created if it does not exist.

    Args:
        filename (str): The path of the file to write.
        text (str): The text to write.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
