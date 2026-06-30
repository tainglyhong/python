numbers = (1, 2, 3)
numbers[0] = 100     # Error

# but if a tuple contain a lists, that inner object in the list can still change
t = (1, [2, 3])
t[1].append(4)

print(t) 

# Looping Through a Tuple

fruits = ("apple", "banana", "cherry")

for fruit in fruits:
    print(fruit)