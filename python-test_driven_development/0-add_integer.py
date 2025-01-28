#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: The first integer or float.
        b: The second integer or float, default is 98.

    Returns:
        The addition of a and b as an integer.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast to int if the inputs are floats
    a = int(a)
    b = int(b)

    return a + b
