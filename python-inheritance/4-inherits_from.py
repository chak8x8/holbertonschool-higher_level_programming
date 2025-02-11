#!/usr/bin/python3
"""Module defining a function to check
if an object is an instance of a subclass."""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a subclass of a specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class,
        otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
