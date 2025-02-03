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
    while i < len(text):
        print(text[i], end="")  # Print the character

        if text[i] in ".?:":  
            print("\n")  # Print **two new lines** after `. ? :`
            print("\n")
            i += 1  # Move to the next character

            while i < len(text) and text[i] == " ":
                i += 1  # **Skip extra spaces after `. ? :`**
            continue  # Go to the next character

        i += 1
