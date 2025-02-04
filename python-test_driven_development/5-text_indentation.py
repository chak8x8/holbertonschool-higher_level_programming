#!/usr/bin/python3
"""
This module defines a function that prints a text with 2 new lines
after each occurrence of '.', '?' or ':'.
Each printed line has no leading or trailing whitespace.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' and ':'.

    Args:
        text (str): The input string to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    current_line = ""
    for char in text:
        # Skip any space if we are at the beginning of a new line.
        if char == " " and current_line == "":
            continue

        if char in ".?:":
            # Add the punctuation to the current line.
            current_line += char
            # Print the accumulated line stripped of leading/trailing spaces.
            print(current_line.strip())
            # Print an extra blank line.
            print()
            # Reset for the next line.
            current_line = ""
        elif char == "\n":
            # If a newline is encountered, print the current_line if any.
            if current_line:
                print(current_line.strip())
                current_line = ""
            else:
                print()
        else:
            current_line += char

    # Print any remaining text (without extra newline at the end).
    if current_line:
        print(current_line.strip(), end="")
