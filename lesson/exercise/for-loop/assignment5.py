# Write a Python program that:
# Loops through numbers from 1 to 100
# Skips all multiples of 5 using continue
# Stops the loop when the number reaches 95 using break

# Displays:

# Even numbers
# Odd numbers

# Counts:

# Total even numbers
# Total odd numbers

even = 0
odd = 0
for i in range(100):

    if i == 95:
        print(f"{i} break out from loop when reaches this number.")
        break

    if i % 5 == 0:
        print(f"{i} skip this number.")
        continue

    if i % 2 == 0:
        print(f"{i} is a even number.")
        even += 1
    else:
        print(f"{i} is a odd number.")
        odd += 1

print(f"Total of even number is {even}")
print(f"Total of odd number is {odd}")
