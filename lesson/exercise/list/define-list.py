# ======================================
# DATA STRUCTURES AND ALGORITHMS
# ======================================
# Concept data structure and algorithm
# What are they?
# Algorithms : a set of rule or step by step to solving problem.
# Data structures : a particular way of organizing data in a computer.

# ======================================
# WHAT IS A LIST?
# ======================================
# List is a kind of collection of data
# - A collection allow us to put many values in a single “variable”
# - A collection is nice because we can carry many values around in one convenient package.
# - List constants are surrounding by [] and seperate each element by commas(,)
# - List can be empty


objects = ["Mouse", "Keyboard", "Computer", "Monitor"]

fruits = ['apple', 'banana', 'orange', 'watermelon']

numbers = [1, 20, 34, 12, 49, 39.22, 99.33]

mixed = ['A', 'Apple', 23, 45.33]

list_in_list = [1, [34, 32], 23]

print(objects)
print(fruits)
print(numbers)
print(mixed)

# ======================================
# EMPTY LIST
# ======================================
empty_list = []
print(empty_list)

# ======================================
# NESTED LISTS
# ======================================
matrix = [
    [1, 2, 3],  # Row 0
    [4, 5, 6],  # Row 1
    [7, 8, 9]   # Row 2
]

print(matrix[0])     # Output: [1, 2, 3] (Fetches the entire first row)
print(matrix[1][1])  # Output: 5         (Fetches row 1, column 1)
print(matrix[2][0])  # Output: 7         (Fetches row 2, column 0)