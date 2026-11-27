#!/usr/bin/python3
"""This module defines a function that lists the attributes of an object."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: Any Python object (an instance, a class, a module, etc.).

    Returns:
        list: The sorted names of the attributes and methods of obj.
    """
    return dir(obj)
