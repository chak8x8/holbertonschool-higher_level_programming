#!/usr/bin/python3
"""
This module defines a function that formats text with indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of '.', '?', and ':'.

    Args:
        text (str): The input text to format.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> text_indentation("Hello. How are you? I am fine: thank you.")
        Hello.

        How are you?

        I am fine:

        thank you.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    text_len = len(text)
    while i < text_len:
        # Print current character
        print(text[i], end="")

        # If it's punctuation, add 2 newlines unless it's the last character
        if text[i] in ".?:":
            if i != text_len - 1:
                print("\n")  # effectively 2 newlines total
            i += 1
            # Skip spaces
            while i < text_len and text[i] == " ":
                i += 1
            continue

        i += 1
