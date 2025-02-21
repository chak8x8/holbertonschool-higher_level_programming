#!/usr/bin/python3
"""Returns the dictionary description of an object for JSON serialization."""


def class_to_json(obj):
    """
    Returns a dictionary description of an object's attributes
    for JSON serialization.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary containing all serializable attributes.
    """
    return obj.__dict__
