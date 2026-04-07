"""
# Exercise 7: Number Guessing Game
Write a program that perform the action below:

computer generate a random number between 1 to 20
user have 5 attempts to guess the number
give a hint to user if the guess is too low or too high

what we need to do:
using while loop with break
track remaining attempts
handle invalid input (non-numeric input and numbers outside the range)
"""


import random

# randint(a, b) will generate a random integer N such that a <= N <= b
guess_number = random.randint(1, 20)

attempts = 5

while attempts > 0:
    try:
        user_guess = input("Guess the number between 1 and 20 : ")
        user_guess = int(user_guess)
        
        if user_guess == guess_number:
            print(f"Congratulations! You guessed the number {guess_number}!")
            break
        elif user_guess < guess_number:
            print("Too low! Try again.")
        elif user_guess > guess_number:
            print("Too high! Try again.")
            
        attempts -= 1
        print(f"Remaining attempts: {attempts}")
        

    except ValueError:
        print("Invalid input. Please enter a number between 1 and 20.")
        continue