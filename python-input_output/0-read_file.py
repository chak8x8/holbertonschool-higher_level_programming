#!/usr/bin/python3
"""Defines a function to read a text file and print its contents."""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read.
        Defaults to an empty string.

    The function:
    - Uses the 'with' statement to handle file closing automatically.
    - Reads the entire content of the file.
    - Prints the content directly to stdout.
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")  # end="" prevents extra newlines
