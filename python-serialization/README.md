Python - Serialization
=====================

- Novice
- By: Javier Valenzani
- Weight: 1
- Your score will be updated as you progress.

Description
-----------

For this project, we expect you to look at these concepts:

- **OOP - Marshaling and Serialization**
- **C - Marshaling and Byte Order**
- **Python - Serialization**

### Introduction

Welcome to our exploration of **marshaling** and **serialization**, two fundamental concepts in computer science that enable the efficient storage and transmission of data. In this programming project, you will delve deep into how data can be transformed and communicated between different parts of a system, or even across different systems. This project is designed to enhance your understanding and practical skills in handling data in real-world applications.

- **What is Marshaling?**  
  Marshaling is the process of transforming memory objects into a format that can be stored or transmitted over a network. It involves packaging complex objects and their attributes into a simpler, often binary, format. This is crucial in scenarios such as remote procedure calls, where objects need to be represented in a standard format across different computing platforms.

- **What is Serialization?**  
  Serialization, closely related to marshaling, specifically involves converting data structures or object states into a format that can be easily saved to a file or sent over a network. The main goal of serialization is to preserve the state of an object so it can be recreated in an identical state elsewhere. This becomes essential in developing applications that require data persistence, distributed computing, and data sharing between different software components.

### Learning Objectives

- Articulate the differences and similarities between **marshaling** and **serialization**.
- Implement **serialization** in a practical programming task.
- Understand how serialized data can be used in web applications, databases, and network communications.
- Evaluate the performance implications of different serialization formats, like JSON, XML, and binary formats.

### Resources

- [Real Python Serialization](#)
- [Real Python: Working With JSON Data in Python](#)
- [Python’s pickle documentation](https://docs.python.org/3/library/pickle.html)
- [Corey Schafer on Pickle](#)
- [CSV to JSON in Python](#)
- [Python XML ElementTree Guide](https://docs.python.org/3/library/xml.etree.elementtree.html)
- [Socket Programming Guide](#)

This project will equip you with the skills needed to manipulate and manage data effectively, preparing you for more advanced topics in computer science and software development. Get ready to build a solid foundation in data handling that will support your future projects and career in the technology sector.

Tasks
-----

### 0. Basic Serialization

**mandatory**

Create a basic serialization module that adds the functionality to serialize a Python dictionary to a JSON file and deserialize the JSON file to recreate the Python dictionary.

**Instructions**:

- Write a Python module named `task_00_basic_serialization.py` with the following functions:
  - `serialize_and_save_to_file(data, filename)`
  - `load_and_deserialize(filename)`

- **`serialize_and_save_to_file(data, filename)`**:
  - `data`: A Python dictionary containing data.
  - `filename`: The output JSON file. If the file already exists, it should be **replaced**.

- **`load_and_deserialize(filename)`**:
  - `filename`: The JSON file to read.
  - Returns a Python dictionary with the **deserialized** JSON data from the file.

**Execution Output Example**:

```
#!/usr/bin/env python3
from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

# Sample data to be serialized
data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Serialize the data to JSON and save it to a file
serialize_and_save_to_file(data_to_serialize, 'data.json')

# Output: The data has been serialized and saved to 'data.json'
print("Data serialized and saved to 'data.json'.")

# Load and deserialize data from 'data.json'
deserialized_data = load_and_deserialize('data.json')

# Output: The deserialized data
print("Deserialized Data:")
print(deserialized_data)
```
```
Data serialized and saved to 'data.json'.
Deserialized Data:
{'name': 'John Doe', 'age': 30, 'city': 'New York'}
```
**Repo:**

- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-serialization`
- File: `task_00_basic_serialization.py`

---

### 1. Pickling Custom Classes

**mandatory**

Learn how to serialize and deserialize **custom Python objects** using the **pickle** module.

**Instructions**:

1. Create a **custom Python class** named `CustomObject` with the following attributes:
   - `name` (string)
   - `age` (integer)
   - `is_student` (boolean)

   Additionally, the class should have a **display** method to print out the object’s attributes, for example:
   ```
   Name: John
   Age: 25
   Is Student: True
   ```

2. Implement two methods within this class:
- `serialize(self, filename)`:  
  Uses the `pickle` module to serialize the current instance and save it to `filename`.
- `@classmethod deserialize(cls, filename)`:  
  Uses the `pickle` module to load and return a `CustomObject` from the specified `filename`.  
  If the file is non-existent or malformed, return **None**.

3. Save your code in `task_01_pickle.py`.

Make sure to handle possible exceptions for non-existent or malformed files. If this happens, the methods should return `None`.

**Sample Test**:
```
#!/usr/bin/env python3
from task_01_pickle import CustomObject

# Create an instance of CustomObject
obj = CustomObject(name="John", age=25, is_student=True)
print("Original Object:")
obj.display()

# Serialize the object
obj.serialize("object.pkl")

# Deserialize the object into a new instance
new_obj = CustomObject.deserialize("object.pkl")
print("\nDeserialized Object:")
new_obj.display()
```
Output:
```
Original Object:
Name: John
Age: 25
Is Student: True

Deserialized Object:
Name: John
Age: 25
Is Student: True
```

**Repo:**

- GitHub repository: `holbertonschool_higher_level_programming`
- Directory: `python-serialization`
- File: `task_01_pickle.py`

---

### 2. Converting CSV Data to JSON Format

**mandatory**

The objective of this exercise is to gain experience in reading data from one format (**CSV**) and converting it into another (**JSON**) using serialization techniques.

**Instructions**:

- Begin by importing the required modules (e.g., `csv`, `json`).
- Define a function named `convert_csv_to_json(csv_filename)` that:
  1. Opens and reads the CSV file using `csv.DictReader`.
  2. Converts each row into a dictionary.
  3. Serializes the list of dictionaries into JSON.
- Writes the serialized JSON to a file named `data.json`.
- Returns `True` if the conversion succeeded, or `False` if an exception (like file not found) occurs.
- Save your work in **`task_02_csv.py`**.

**Testing Your Code:**:
```
```
```
```

**CSV Dataset (`data.csv`) example:**:
```
```
After the conversion, the resulting `data.json` file should contain:
```
```

**Repo:**

- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-serialization`
- File: `task_02_csv.py`

---

### 3. Serializing and Deserializing with XML

**mandatory**

In this exercise, we explore **serialization** and **deserialization** using **XML** as an alternative to JSON.

**Instructions**:
- Begin by importing the required modules. You can use the xml.etree.ElementTree module which is a part of Python’s standard library for XML processing:
```
import xml.etree.ElementTree as ET
```
- Define two main functions:
    1. `serialize_to_xml(dictionary, filename)`: This will take a Python dictionary and a filename as parameters. It should serialize the dictionary into XML and save it to the given filename.
    2. `deserialize_from_xml(filename)`: This will take a filename as its parameter, read the XML data from that file, and return a deserialized Python dictionary.

- For serialize_to_xml:
    1. Create a root element, e.g., `<data>`.
    2. Iterate through the dictionary items and add them as child elements to the root.
    3. Write the XML tree to the provided filename using the `ET.ElementTree` class.

- For deserialize_from_xml:
    1. Parse the XML file using `ET.parse`.
    2. Navigate through the XML elements to reconstruct the dictionary.
    3. Return the constructed dictionary.

- Be cautious about data types. XML doesn’t differentiate between numbers and strings, etc., like Python does. You might need to manage type conversions.

- Save your work in `task_03_xml.py`.

**Testing Your Code:**:
```
#!/usr/bin/env python3
from task_03_xml import serialize_to_xml, deserialize_from_xml

def main():
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)

if __name__ == "__main__":
    main()
```
**Output::**:
```
Dictionary serialized to data.xml

Deserialized Data:
{'name': 'John', 'age': '28', 'city': 'New York'}
```
data.xml
```
<data>
    <name>John</name>
    <age>28</age>
    <city>New York</city>
</data>
```

**Repo:**

- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-serialization`
- File: `task_03_xml.py`