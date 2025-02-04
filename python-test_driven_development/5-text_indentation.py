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

    result = []  # This list will hold the lines to be printed.
    current_line = ""
    i = 0
    while i < len(text):
        # Skip any leading spaces for a new sentence.
        if text[i] == " " and current_line == "":
            i += 1
            continue

        if text[i] in ".?:":
            # Append the punctuation to the current sentence.
            current_line += text[i]
            # Append the sentence (stripped) to the result.
            result.append(current_line.strip())
            # Look ahead to see
            # if there is any non-space character after the punctuation.
            j = i + 1
            while j < len(text) and text[j] == " ":
                j += 1
            # If there is more text,
            # add an empty string to produce a blank line.
            if j < len(text):
                result.append("")
            # Reset the accumulator and update the index.
            current_line = ""
            i += 1
            continue

        else:
            # Otherwise, accumulate the character.
            current_line += text[i]
        i += 1

    # If anything remains in the accumulator, add it.
    if current_line:
        result.append(current_line.strip())

    # Print all lines. To avoid a trailing newline,
    # the last line is printed with end="".
    for idx, line in enumerate(result):
        if idx == len(result) - 1:
            print(line, end="")
        else:
            print(line)
