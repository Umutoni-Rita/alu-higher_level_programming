#!/usr/bin/python3
"""This module defines a function that checks for a strict subclass instance.
"""


def inherits_from(obj, a_class):
    """Check whether an object belongs to a strict subclass of a given class.

    The object must be an instance of a class that inherited (directly or
    indirectly) a_class, but must not be an instance of a_class itself.

    Args:
        obj: The object to check.
        a_class: The parent class to compare against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class,
            otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
