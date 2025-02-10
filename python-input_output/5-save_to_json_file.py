#!/usr/bin/python3
"""
Module for save_to_json_file
"""


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation
    """
    import json
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
