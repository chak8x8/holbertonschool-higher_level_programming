#!/usr/bin/python3
"""Script that adds command-line arguments
to a list and saves them to a JSON file."""

import sys

# Dynamically import functions
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    # Try loading the existing list from the file
    items = load_from_json_file(filename)
except FileNotFoundError:
    # If file does not exist, initialize an empty list
    items = []

# Extend the list with command-line arguments (excluding the script name)
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
