#!/usr/bin/python3
"""
This module provides add_integer, a function that adds two numbers.
Floats are cast to integers before the addition is performed.
Any argument that is not an integer or a float raises a TypeError.
"""


def add_integer(a, b=98):
    """Return the integer sum of a and b (b defaults to 98).
    Floats are cast to int first; any other type raises a TypeError.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
