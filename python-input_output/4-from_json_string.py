#!/usr/bin/python3
"""This module defines a function that turns a JSON string into an object."""
import json


def from_json_string(my_str):
    """Return the Python data structure represented by a JSON string.

    Args:
        my_str (str): The JSON text to decode.

    Returns:
        The Python object (dict, list, str, int, ...) described by my_str.
    """
    return json.loads(my_str)
