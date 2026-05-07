# Dictionary
# keys are unique and immutable, values can be duplicate and mutable
# syntax: dict_name = {key1: value1, key2: value2, ...}

# Creating a dictionary
persons = {
    "name": "Alice", 
    "age": 30,
    "city": "New York"
}

# Accessing values
print(persons["name"])  # Output: Alice
print(persons["age"])   # Output: 30
print(persons["city"])  # Output: New York

# Adding a new key-value pair
persons["job"] = "Engineer"
print(persons)

# Updating an existing value
persons["age"] = 31
print(persons["age"])

# Removing a key-value pair
del persons["city"]
print(persons)

# Essential dictionary methods
# Get all keys
print(persons.keys())  # Output: dict_keys(['name', 'age', 'job'])

# Get all values
print(persons.values())  # Output: dict_values(['Alice', 31, 'Engineer'])

# Get all key-value pairs
print(persons.items())  # Output: dict_items([('name', 'Alice'), ('age', 31), ('job', 'Engineer')])

# update()
new_info = {"age": 32, "city": "Los Angeles"}
persons.update(new_info)

# clear()
persons.clear()
print(persons)  # Output: {}