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

avatar.draw_bow()
avatar.draw_eyes("medium")
avatar.draw_nose("triangle")
avatar.draw_mouth("smile")
