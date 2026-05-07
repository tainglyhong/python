# Tuple 
# Tuple is an ordered, immutable collection of items.
# imutable is a data type that cannot be changed after it is created.

# syntax: tuple_name = (item1, item2, item3, ...)

numbers = (1, 2, 3, 4, 5)

fruits = ("apple", "banana", "cherry")

mixed_tuple = (1, "hello", 3.14, True)

empty_tuple = ()

single_element_tuple = (42,)  # Note the comma for single element

# single_element_tuple = (42) # This would be just an integer, not a tuple 

print(type(single_element_tuple))

print(fruits[0])  # Accessing first element

fruit = ("mango", )

my_fruits = fruits + fruit  # Concatenating tuples

print(my_fruits)