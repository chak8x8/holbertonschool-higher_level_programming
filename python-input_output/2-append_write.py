#!/usr/bin/python3
"""Defines a function to append a string to a text file."""


def append_write(filename="", text=""):
    """Appends a string at the end of a UTF-8 text file
    and returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        Defaults to an empty string.
        text (str): The text to append.
        Defaults to an empty string.

    Returns:
        int: The number of characters added.

    The function:
    - Uses the 'with' statement for safe file handling.
    - Opens the file in 'a' mode (append mode).
    - Creates the file if it does not exist.
    - Appends the given text to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)  # Returns the number of characters added
