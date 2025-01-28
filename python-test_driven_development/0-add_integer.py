#!/usr/bin/python3
"""
This module provides a function `add_integer` that adds two integers.

The `add_integer` function:
- Casts inputs to integers if they are floats.
- Raises a TypeError if inputs are not integers or floats.
- Returns the sum of two integers.
"""
def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
