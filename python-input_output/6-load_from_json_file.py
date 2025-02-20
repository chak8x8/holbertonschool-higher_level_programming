#!/usr/bin/python3
"""Defines a function that loads an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Reads a JSON file and returns the corresponding Python object.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        any: The Python object (dict, list, etc.) deserialized
        from the JSON file.

    Example:
    >>> my_list = load_from_json_file("my_list.json")
    >>> print(my_list)  # Output: [1, 2, 3]

    >>> my_dict = load_from_json_file("my_dict.json")
    >>> print(my_dict)  # Output: {'name': 'John', 'age': 30}

    Notes:
    - The function **assumes** that `filename` exists and contains valid JSON.
    - If the file contains invalid JSON, `json.JSONDecodeError` will be raised.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)  # Correctly reads and parses JSON from file
