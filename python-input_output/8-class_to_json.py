#!/usr/bin/python3
"""This module defines a function that describes an object as a dictionary.
"""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON serialization.

    Args:
        obj: An instance of a class whose attributes are all simple,
            serializable types (list, dict, str, int, bool).

    Returns:
        dict: The instance attributes of obj, keyed by attribute name.
    """
    return obj.__dict__
