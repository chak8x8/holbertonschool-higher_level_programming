#!/usr/bin/python3
"""Defines a function that converts a JSON string to a Python object."""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to be converted into a Python object.

    Returns:
        object: A Python object (list, dict, int, etc.)
        corresponding to the JSON string.

    Example:
    >>> from_json_string('{"name": "Alice", "age": 25}')
    {'name': 'Alice', 'age': 25}

    >>> from_json_string("[1, 2, 3]")
    [1, 2, 3]

    Note:
    - The function does not handle JSON decoding errors.
    If `my_str` is not a valid JSON string,
      `json.loads()` will raise a `JSONDecodeError`.
    """
    return json.loads(my_str)  # Converts JSON string to Python object
