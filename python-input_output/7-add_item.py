#!/usr/bin/python3
"""This script adds all command-line arguments to a list saved as JSON.

The list is stored in add_item.json; each run appends the new arguments
to the list already saved there, creating the file when it is missing.
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    filename = "add_item.json"
    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)
