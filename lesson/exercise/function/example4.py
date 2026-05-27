import random

def roll_dice(num_dice, num_sides):
    """Rolls the given set of dice and returns the total."""
    total = 0
    for die in range(num_dice):
        total = total + random.randint(1, num_sides)
    return total


roll = roll_dice(1, 6) + roll_dice(1, 6)

print("You rolled a total of " + str(roll))
