"""
Project/File Name: CS 211: Module 2 Coding Demo - Lists, Arrays, Dictionaries
Author:           Marc Robertson
Date Created:     August 24, 2025
Last Modified:    August 27, 2025

Purpose:          Demo the concepts of Lists, Arrays, Dictionaries by practical application

Dependencies:     Array module
Usage:            [How to run or use this file/project]
Inputs:           [Describe expected input, if any]
Outputs:          [Describe output, if any]
Notes:            [Any additional important information]
"""

# ------------------------------
# Dcitionary Section
# ------------------------------

# Function to declare a dictionary
def dictionary():
    return {}  # Returns an empty dictionary

# Function to insert a key-value pair
def InsertKeyValue(dict, key, value):
    dict[key] = value

# Function to update value for an existing key
def UpdateValue(dict, key, new_value):
    if key in dict:
        dict[key] = new_value
    else:
        print(f"Key '{key}' not found")

# Function to delete a key-value pair
def DeleteKey(dict, key):
    if key in dict:
        del dict[key]
    else:
        print(f"Key '{key}' not found")

# Function to search for a value by key
def SearchByKey(dict, key):
    return dict.get(key, "Key not found")

# Function to display the dictionary
def DisplayDictionary(dict):
    if not dict:
        print("Dictionary is empty")
    else:
        for key, value in dict.items():
            print(f"{key} : {value}")

# ------------------------------
# Each case for dictionary manipulation
# ------------------------------

dict = dictionary()

# Insert key-value pairs
InsertKeyValue(dict, "name", "Marc")
InsertKeyValue(dict, "age", 25)
InsertKeyValue(dict, "city", "New York")

print("Dictionary after insertions:")
DisplayDictionary(dict)

# Update and delete operations
UpdateValue(dict, "age", 26)
DeleteKey(dict, "city")

print("\nDictionary after updates and deletion:")
DisplayDictionary(dict)

# Search examples
print("\nSearch 'name':", SearchByKey(dict, "name"))
print("Search 'city':", SearchByKey(dict, "city"))
