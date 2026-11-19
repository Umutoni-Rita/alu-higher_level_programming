#!/usr/bin/python3
"""This module defines a function that converts an object to a JSON string."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object as a string.

    Args:
        my_obj: A JSON-serializable Python object (dict, list, str, ...).

    Returns:
        str: The JSON text that represents my_obj.
    """
    return json.dumps(my_obj)
