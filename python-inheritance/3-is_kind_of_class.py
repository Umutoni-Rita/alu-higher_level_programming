#!/usr/bin/python3
"""This module defines a function that checks if an object is a kind of class.
"""


def is_kind_of_class(obj, a_class):
    """Check whether an object is an instance of a class or of its subclass.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or of a class that
            inherited it, otherwise False.
    """
    return isinstance(obj, a_class)
