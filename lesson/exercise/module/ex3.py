import random

result = random.randint(1, 10)

# The team has a 20% chance of a win, a 30% chance of a loss, 
# and a 50% chance of a tie.

if result == 1 or result == 2:
    match_end = "WIN"
elif result <= 5:
    match_end = "LOSS"
else:
    match_end = "TIE"

print("The result of number : " + str(result))
print("The team finished with a " + match_end)
