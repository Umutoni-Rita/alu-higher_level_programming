#!/usr/bin/python3
"""This module defines a function that creates an object out of a JSON file.
"""
import json


def load_from_json_file(filename):
    """Create a Python object by decoding the JSON content of a file.

    Args:
        filename (str): The path of the JSON file to read.

    Returns:
        The Python object described by the file's JSON content.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
