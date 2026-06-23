import random
"""Supports a round of rock, paper, scissors between a user and a computer."""

def make_user_choice():
    """Returns the user's choice of rock, paper, or scissors."""
    choice = input("Choose one: rock, paper, scissors? ")
    
    while choice != "rock" and choice != "paper" and choice != "scissors":
        print("Invalid choice. Try again.")
        choice = input("Choose one: rock, paper, scissors? ")
        
    return choice

def make_computer_choice():
    """Returns the computer's random choice of rock, paper, or scissors."""
    number = random.randint(1,3)
    if number == 1:
        return 'rock'
    elif number == 2:
        return 'paper'
    else:
        return 'scissors'

def wins_matchup(choice, opponent_choice):
    """Returns True if the first player's choice wins over their opponent.

    Choices can be rock, paper, or scissors. Assumes the choices are different.
    """
    return (
        (choice == "rock" and opponent_choice == "scissors") or
        (choice == "scissors" and opponent_choice == "paper") or
        (choice == "paper" and opponent_choice == "rock")
    )

def format_score(user_score, computer_score):
    """Returns a formatted version of the players's current scores."""
    return ">> Score: " + str(user_score) + "-" + str(computer_score)
