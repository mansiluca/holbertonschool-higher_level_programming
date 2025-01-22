#!/usr/bin/python3
"""
Module for text_indentation
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', or ':'.
    Args:
        text: string
    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']
    result = ""
    skip_spaces = False

    for char in text:
        if skip_spaces and char == ' ':
            continue
        skip_spaces = False
        result += char
        if char in characters:
            result += "\n\n"
            skip_spaces = True

    print(result.strip(), end="")
