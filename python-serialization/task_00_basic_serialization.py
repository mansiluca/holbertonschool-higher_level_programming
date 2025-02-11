#!/usr/bin/python3
"""
Module for task_00_basic_serialization
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    serializes an object to a text file, using a JSON representation
    """
    with open(filename, mode='w', encoding=None) as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    deserializes a JSON representation from a text file
    """
    with open(filename, mode='r', encoding=None) as f:
        return json.load(f)
