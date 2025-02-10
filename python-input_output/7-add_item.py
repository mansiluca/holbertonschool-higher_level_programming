#!/usr/bin/python3
"""
Module for add_item
"""


from sys import argv
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"

if __name__ == "__main__":
    if path.exists(file):
        my_list = load_from_json_file(file)
    else:
        my_list = []
    my_list.extend(argv[1:])
    save_to_json_file(my_list, file)
