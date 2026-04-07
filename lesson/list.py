# List (data structure)
# A list is a collection of items that are ordered and changeable. 
# In Python, 
# lists are defined using square brackets [] and can contain elements of different data types.

# syntax: list_name = [item1, item2, item3, ...]

my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

# Methods to manipulate lists

# Accessing elements
print("First element:", my_list[0])  # Index starts at 0
print("Last element:", my_list[-1])  # Negative index for last element

# Modifying elements
my_list[2] = 10
print("Modified List:", my_list)

# Adding elements
my_list.append(6)  # Adds 6 to the end of the list
print("List after appending 6:", my_list)

# Inserting elements
my_list.insert(1, 15)  # Inserts 15 at index 1
print("List after inserting 15 at index 1:", my_list)

# Removing elements
my_list.remove(10)  # Removes the first occurrence of 10
print("List after removing 10:", my_list)

# Sorting the list
my_list.sort()  # Sorts the list in ascending order
print("Sorted List:", my_list)

# Popping elements
# pop() last in 
popped_element = my_list.pop()  # Removes and returns the last element
print("Popped element:", popped_element)
print("List after popping an element:", my_list)

# Slicing
sliced_list = my_list[1:4]  # Gets elements from index 1 to 3
print("Sliced List (index 1 to 3):", sliced_list)

# Length of the list
length = len(my_list)
print("Length of the list:", length)

# Concatenation
another_list = [7, 8, 9]
concatenated_list = my_list + another_list
print("Concatenated List:", concatenated_list)

# Repetition
repeated_list = my_list * 2  # Repeats the list twice
print("Repeated List:", repeated_list)

