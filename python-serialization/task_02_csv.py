#!/usr/bin/env python3
"""Module for converting CSV data to JSON format."""

import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Reads a CSV file and converts its contents to JSON format.
    
    Args:
        csv_filename (str): The name of the CSV file to read.

    Returns:
        bool: True if conversion is successful, False if an error occurs.
    """
    try:
        with open(csv_filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            data = list(reader)
            
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)
            
        return True

    except FileNotFoundError as e:
        print("Error: {}".format(e))
        return False
