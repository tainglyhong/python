"""
1.  # Import the random module and use random.randint(1, 2)
    # to randomly choose and draw either a "triangle" nose
    # or a "button" nose for the avatar, with equal chance.

2.  # Use random.randint(1, 4) to randomly choose the avatar's mouth.
    # Draw "smile", "teeth", or "neutral", where "smile"
    # has a higher chance by assigning it to two numbers.
    
3.  # Use random.randint(1, 3) to randomly choose the bow location.
    # The avatar can have a hair bow, a bowtie, or no bow,
    # with each option equally likely.
    # Draw the hair bow before the face features,
    # draw the bowtie after the face features,
    # and make sure only one bow option is chosen.
"""

import avatar
import random

bow = random.randint(1,3)
if bow == 1:
    avatar.draw_bow()

avatar.draw_eyes("medium")

nose = random.randint(1,2)
if nose == 1:
    avatar.draw_nose("triangle")
else:
    avatar.draw_nose("button")

mouth = random.randint(1,4)
if mouth == 1 or mouth == 2:
    avatar.draw_mouth("smile")
elif mouth == 3:
    avatar.draw_mouth("teeth")
else:
    avatar.draw_mouth("neutral")
    
if bow == 2:
    avatar.draw_bow()
    