#!/usr/bin/python3
"""Script that adds all command-line arguments to a list and saves them to a JSON file"""

import sys
from 5-save_to_json_file.py import save_to_json_file
from 6-load_from_json_file.py import load_from_json_file

filename = "add_item.json"

try:
    # Load existing list from file if it exists
    items = load_from_json_file(filename)
except FileNotFoundError:
    # If the file doesn't exist, initialize an empty list
    items = []

# Append all command-line arguments except the script name
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
