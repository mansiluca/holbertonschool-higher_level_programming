#!/usr/bin/python3
def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”
    """
    import json
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
