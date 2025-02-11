#!/usr/bin/python3
"""Module defining a function to check inheritance."""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a specified class
    or an instance of a subclass of that class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or its subclass, else False.
    """
    return isinstance(obj, a_class)
