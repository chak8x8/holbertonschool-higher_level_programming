#!/usr/bin/python3
"""
This module defines a function that prints a text with 2 new lines after
each occurrence of '.', '?' and ':'.
Each printed line has no space at the beginning or at the end.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' and ':'.

    Args:
        text (str): The text to format and print.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    # Remove any leading and trailing whitespace from the entire text.
    text = text.strip()
    new_line = True  # Flag: are we at the beginning of a new line?

    for char in text:
        # When encountering one of the target punctuation characters,
        # print it, then print a newline (which, together with print's own
        # newline, produces 2 newlines), and mark that we're at a new line.
        if char in ".?:":
            print(char, end="")
            print("\n")
            new_line = True
        # If a newline appears in the text, print it and mark that we're at a new line.
        elif char == "\n":
            print()
            new_line = True
        else:
            # Skip any space if it would be at the beginning of a new line.
            if new_line and char == " ":
                continue
            print(char, end="")
            new_line = False
