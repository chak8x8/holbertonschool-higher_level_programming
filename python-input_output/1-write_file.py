#!/usr/bin/python3
"""Defines a function to write a string to a text file."""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 text file
    and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        Defaults to an empty string.
        text (str): The text to write into the file.
        Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.

    The function:
    - Uses the 'with' statement to handle file operations safely.
    - Opens the file in 'w' mode (overwrite mode).
    - Creates the file if it does not exist.
    - Overwrites existing content if the file already exists.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)  # Returns the number of characters written
