import random

roll_total = 0
roll = 0

# Aim for the highest roll total before rolling a 1.
while roll != 1:
    roll_total = roll_total + roll

    roll = random.randint(1, 6)
    print("You rolled a " + str(roll))

print("Your roll streak was " + str(roll_total))
