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
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = []     # Will hold the lines to print.
    current_line = ""
    i = 0

    while i < len(text):
        char = text[i]
        # Skip leading spaces for a new line.
        if char == " " and current_line == "":
            i += 1
            continue

        # When a punctuation character is found...
        if char in ".?:":
            current_line += char
            # Look ahead: skip any spaces after the punctuation.
            j = i + 1
            while j < len(text) and text[j] == " ":
                j += 1
            # Append the current sentence (trimmed) to the result.
            result.append(current_line.strip())
            # If there is more text after the punctuation,
            # add an empty line (to produce 2 newlines).
            if j < len(text):
                result.append("")
            # Reset current_line and update the index.
            current_line = ""
            i += 1
            continue

        # For all other characters, add them to current_line.
        else:
            current_line += char
        i += 1

    # If any text remains after the loop, add it.
    if current_line:
        result.append(current_line.strip())

    # Print all lines.
    # To avoid a trailing newline, the last line is printed with end="".
    for idx, line in enumerate(result):
        if idx == len(result) - 1:
            print(line, end="")
        else:
            print(line)
