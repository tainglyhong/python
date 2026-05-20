import random

p1_wins = 0
p2_wins = 0

# The first player to win 3 rounds wins the game.
while p1_wins < 3 and p2_wins < 3:
    winner = random.randint(1, 2)
    
    if winner == 1:
        print("Player 1 wins!")
        p1_wins += 1
    else:
        print("Player 2 wins!")
        p2_wins += 1