import random

# Roll a fair six-sided dice.
first_roll = random.randint(1, 6)
print(f"You rolled a {first_roll}")

# Only roll again if the first roll was a 1, 2, or 3.
if first_roll <= 3:
    second_roll = random.randint(1, 6)
    print("You rolled a " + str(second_roll))
