# Random elements
import random

colors = ["red", "orange", "yellow", "green", "blue"]

color = random.choice(colors)

print("You chose " + color + "!")


#build list from scratch
# - We can create an empty list and 
# then add elements using the append method
# - The list stays in order and 
# new elements are added at the end of the list

staff = list()

staff.append("Hong")
staff.append("Hour")
staff.append("Heng")

# Add a list specific index
staff.insert(1, "Sav")
print(staff)

# find item in a list using in 
somes = [1, 2, 4, 5]
print(somes)

print(5 in somes)
print(32 in somes)

#you can sorting a list in order
somes.sort()
print("After sorting : ", somes)

#remove
somes.remove(5)
print(somes)