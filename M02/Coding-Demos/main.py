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

# ------------------------------
# Array section
# ------------------------------


# Insert an element at the end
def InsertAtEnd(arr, value):
    arr.append(value)

# Insert an element at the beginning
def InsertAtBeginning(arr, value):
    arr.insert(0, value)

# Insert an element in the middle
def InsertAtMiddle(arr, value):
    pos = len(arr) // 2
    arr.insert(pos, value)

# Delete an element from the end
def DeleteFromEnd(arr):
    if arr:
        arr.pop()

# Delete an element from the beginning
def DeleteFromBeginning(arr):
    if arr:
        arr.pop(0)

# Delete an element from the middle
def DeleteFromMiddle(arr):
    if arr:
        pos = len(arr) // 2
        for i in range(pos, len(arr) - 1):
            arr[i] = arr[i + 1]
        arr.pop()

# Search for an element
def SearchElement(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1

# Display array (one element per line)
def DisplayArray(arr):
    for element in arr:
        print(element)

# ------------------------------
# Each case for array manipulation
# ------------------------------

arr = [10, 20, 30]
print("Initial array:")
DisplayArray(arr)

InsertAtEnd(arr, 40)
print("\nAfter inserting at end:")
DisplayArray(arr)

InsertAtBeginning(arr, 5)
print("\nAfter inserting at beginning:")
DisplayArray(arr)

InsertAtMiddle(arr, 25)
print("\nAfter inserting at middle:")
DisplayArray(arr)

DeleteFromEnd(arr)
print("\nAfter deleting from end:")
DisplayArray(arr)

DeleteFromBeginning(arr)
print("\nAfter deleting from beginning:")
DisplayArray(arr)

DeleteFromMiddle(arr)
print("\nAfter deleting from middle:")
DisplayArray(arr)

# Search for an element (25)
index = SearchElement(arr, 25)
print(f"\nIndex of 25: {index}")

# -------------------------------
# Comparison function
# -------------------------------

def compare_array_vs_dict():
    print("\nComparison: Array vs. Dictionary (for insertion, deletion, and search)")

    # Setup
    arr = list(range(10000))       # Using Python list for array
    dict = {i: i for i in range(10000)}  # Dictionary with same 10000 elements

    # Time insertion at end
    start = time.time()
    arr.append(10000)
    arr_insert_time = time.time() - start

    start = time.time()
    dict[10000] = 10000
    dict_insert_time = time.time() - start

    print(f"Array insert at end: {arr_insert_time:.6f} seconds")
    print(f"Dictionary insert: {dict_insert_time:.6f} seconds")

    # Time deletion from end
    start = time.time()
    arr.pop()
    arr_delete_time = time.time() - start

    start = time.time()
    del dict[10000]
    dict_delete_time = time.time() - start

    print(f"Array delete from end: {arr_delete_time:.6f} seconds")
    print(f"Dictionary delete: {dict_delete_time:.6f} seconds")

    # Time search for element 5000
    start = time.time()
    arr.index(5000)
    arr_search_time = time.time() - start

    start = time.time()
    _ = dict.get(5000)
    dict_search_time = time.time() - start

    print(f"Array search for 5000: {arr_search_time:.6f} seconds")
    print(f"Dictionary search for key 5000: {dict_search_time:.6f} seconds")


# -------------------------------
# Main
# -------------------------------

if __name__ == "__main__":
    # Your previous array demo
    arr = [10, 20, 30]
    print("Initial array:")
    for element in arr:
        print(element)

    # Your previous dictionary demo
    dict = {}
    dict["name"] = "Marc"
    dict["age"] = 25
    dict["city"] = "New York"

    print("\nInitial dictionary:")
    for key, value in dict.items():
        print(f"{key} : {value}")

    # Run comparison
    compare_array_vs_dict()
