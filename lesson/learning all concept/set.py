# Set 

# Syntax: set_name = {item1, item2, item3, ...}

# Creating a set
my_set = {1, 2, 3, 4, 5}

print(type(my_set))  # Output: <class 'set'>

# adding
my_set.add(6)
print(f'After adding 6: {my_set}')

# removing
my_set.remove(3)
print(f'After removing 3: {my_set}')


# two sets example
# set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union
union_set = set_a.union(set_b)
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5, 6}

# intersection
intersection_set = set_a.intersection(set_b)
print("Intersection:", intersection_set)  # Output: {3, 4}

# difference
difference_set = set_a.difference(set_b)
print("Difference :", difference_set)  # Output: {1, 2}

# symmetric difference
sym_diff_set = set_a.symmetric_difference(set_b)
print("Symmetric Difference:", sym_diff_set)  # Output: {1, 2, 5, 6}