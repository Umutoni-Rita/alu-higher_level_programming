#!/usr/bin/python3
"""
This module provides print_square, a function that prints
a square of the given size using the character #.
The size must be an integer greater than or equal to 0.
"""


def print_square(size):
    """Print a square of side length size made of # characters.
    Raise TypeError if size is not an int, ValueError if size < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
