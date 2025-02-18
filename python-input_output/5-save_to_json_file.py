#!/usr/bin/python3
"""Defines a function
that writes an object to a file using JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation.

    Args:
        my_obj (any): The object to be serialized to JSON and saved.
        filename (str): The name of the file to write to.

    Returns:
        None

    Example:
    >>> my_list = [1, 2, 3]
    >>> save_to_json_file(my_list, "my_list.json")

    >>> my_dict = {"name": "Alice", "age": 25}
    >>> save_to_json_file(my_dict, "my_dict.json")

    Notes:
    - The function **overwrites** the file if it already exists.
    - If `my_obj` is not serializable, a `TypeError` will be raised.
    - Uses `with open()` to ensure the file is properly closed after writing.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)  # Writes JSON data to the file
