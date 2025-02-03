#!/usr/bin/python3
"""
This module defines a function that formats text with indentation.
"""


def text_indentation(text):
    """
    Prints `text` with 1 blank line after each '.', '?', ':'.

    Args:
        text (str): The input text to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)
    while i < length:
        print(text[i], end="")  # Print current char (no extra newline)

        if text[i] in ".?:":
            # Just one newline (not an extra blank line)
            print()
            i += 1
            # Skip spaces that come right after punctuation
            while i < length and text[i] == " ":
                i += 1
            continue

        i += 1
