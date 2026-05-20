"""
1.  # Use a while loop to repeat  experiment 10 times.
The two dice should be rolled 10 times, 
and on each of the 10 rolls, the program should print the dice_sum. 
You’ll need to add a loop variable to count to 10 rolls, 
and increment it on each loop iteration.

2.  # Add a new variable at the top of the program to track the running total of all rolls.
On each loop iteration, increment the running total variable by the dice_sum.
At the end of the program, print the average of all ten rolls.

3.  # Use the input() function to ask 
the user how many times they would like to repeat the experiment.
Repeat the while loop the number of times the user entered.
"""
import random

roll = 0
total = 0
roll_time = int(input("Enter a number of roll : "))

while roll < roll_time:
    
    # Roll two six-sided dice.
    first_die = random.randint(1, 6)
    second_die = random.randint(1, 6)

    dice_sum = first_die + second_die
    
    roll = roll + 1
    total = total + dice_sum
    
    print("You rolled a " + str(dice_sum) + "!")

print("The average of 10 rolled is : " + str(total/roll_time))

