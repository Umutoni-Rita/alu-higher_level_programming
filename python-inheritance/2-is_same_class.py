#!/usr/bin/python3
"""This module defines a function that checks the exact class of an object."""


def is_same_class(obj, a_class):
    """Check whether an object is exactly an instance of a given class.

    Instances of subclasses do not count.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the type of obj is exactly a_class, otherwise False.
    """
    return type(obj) is a_class
