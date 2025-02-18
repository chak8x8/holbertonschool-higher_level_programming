#!/usr/bin/python3
"""Defines a function that converts a Python object to a JSON string."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string).

    Args:
        my_obj (any): The object to be converted to JSON format.

    Returns:
        str: JSON string representation of the object.

    Example:
    >>> to_json_string([1, 2, 3])
    '[1, 2, 3]'

    >>> to_json_string({"name": "Alice", "age": 25})
    '{"name": "Alice", "age": 25}'

    Note:
    - If the object cannot be serialized (e.g., a set),
    `json.dumps()` raises a `TypeError`.
    """
    return json.dumps(my_obj)  # Converts Python object to JSON string
