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

    result = []      # List to store the sentences and blank lines.
    current_line = ""
    i = 0

    while i < len(text):
        # Skip spaces at the beginning of a sentence.
        if text[i] == " " and current_line == "":
            i += 1
            continue

        if text[i] in ".?:":
            # Add the punctuation to the current sentence.
            current_line += text[i]
            # Append the sentence (stripped of extra spaces) to the result.
            result.append(current_line.strip())
            # Look ahead: skip spaces after the punctuation.
            j = i + 1
            while j < len(text) and text[j] == " ":
                j += 1
            # If there's still text after the punctuation, append an empty
            # string so that a blank line will be printed.
            if j < len(text):
                result.append("")
            # Reset for the next sentence.
            current_line = ""
            i += 1
            continue
        else:
            current_line += text[i]
        i += 1

    # If any text remains, add it as the final sentence.
    if current_line:
        result.append(current_line.strip())

    # Remove a trailing empty element (if any) so that no extra newline is printed.
    if result and result[-1] == "":
        result.pop()

    # Print each line. The last line is printed without an additional newline.
    for idx, line in enumerate(result):
        if idx == len(result) - 1:
            print(line, end="")
        else:
            print(line)
