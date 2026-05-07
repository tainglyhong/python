"""
Krista and Carmen programmed an avatar module to draw characters for their game. Instead of giving every player the same avatar, they want to randomly generate one at the start of the game.

Use random.randint() to generate a random number between 1 and 2, inclusive.
Use the random number to randomly draw either a triangle or button nose, where each shape is equally likely.
The avatar.draw_nose() function takes one of two possible nose shapes as an argument: "triangle" or "button". One of the numbers should mean you draw a triangle nose and the other number should mean you draw a button nose.

Remember to import the random module at the top of the program!

The avatar can sport one of three mouth options: a smile, a neutral expression, or a big mouth full of teeth. Carmen proposes they draw the avatar with a smile more often, since players prefer happy avatars.

Use random.randint() to generate a random number between 1 and 4, inclusive.
Use the random number to randomly draw either a smile, teeth, or neutral mouth, where a smile is twice as likely.
The avatar.draw_mouth() function takes one of three possible expressions as an argument: "smile", "teeth", or "neutral". To make smiles appear twice as often, you can have two of the four possible numbers correspond to a smile.

Don’t forget to accessorize! Avatars can wear a bow on their head as a hair accessory, wear a bow on their neck as a bowtie, or wear no bow at all.

For a hair bow, the bow needs to be drawn first — before the eyes, nose, and mouth. For a bowtie, the bow needs to be drawn last. For no bow, you'll just skip calling draw_bow() altogether.

Use random.randint() to generate a random number between 1 and 3, inclusive.
Use the random number to randomly choose a bow location, where each location is equally likely.
Be sure to generate a random number to represent the bow location just once. It should not be possible for the avatar to have a hair bow and a bowtie at the same time.

"""

import avatar
import random


rand_bow = random.randint(1,3)
if rand_bow == 1:
    avatar.draw_bow()
    
avatar.draw_eyes("medium")

rand_nose = random.randint(1,2)
if rand_nose == 1:
    avatar.draw_nose("triangle")
else:
    avatar.draw_nose("button")

rand_mouth = random.randint(1,4)
if rand_mouth == 1 or rand_mouth == 2:
    avatar.draw_mouth("smile")
elif rand_mouth == 3:
    avatar.draw_mouth("teeth")
else:
    avatar.draw_mouth("neutral")

if rand_bow == 2:
    avatar.draw_bow()
