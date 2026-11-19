#!/usr/bin/python3
"""This module defines a function that prints the content of a text file."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its content to stdout.

    Args:
        filename (str): The path of the file to read.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
