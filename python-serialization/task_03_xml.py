#!/usr/bin/env python3
"""
Module for serializing and deserializing a dictionary to/from XML.
"""

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.

    Args:
        dictionary (dict): The dictionary to be serialized.
        filename (str): The name of the XML file to write to.

    Returns:
        bool: True if serialization is successful, False otherwise.
    """
    try:
        root = ET.Element("data")  # Root element <data>

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)  # Create child elements
            child.text = str(value)  # Set the text content

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        return True
    except Exception as e:
        print(f"Error serializing to XML: {e}")
        return False

def deserialize_from_xml(filename):
    """
    Deserializes an XML file back into a Python dictionary.

    Args:
        filename (str): The name of the XML file to read from.

    Returns:
        dict: The reconstructed dictionary from XML.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        dictionary = {}
        for child in root:
            dictionary[child.tag] = child.text  # Convert text back to string
        
        return dictionary
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return {}
    except ET.ParseError:
        print(f"Error: Failed to parse XML from '{filename}'.")
        return {}
