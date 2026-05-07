"""
When the code print the message You win a stuffed giraffe!
When the code print the message You win a bouncy ball!
When the code print the message You win a sticker!
When the code print the message You win a bouncy ball!/You win a sticker!
"""

tickets = 29
if tickets >= 60:
    tickets = tickets - 60
    print("You win a stuffed giraffe!")
elif tickets >= 40:
    tickets = tickets - 40
    print("You win a bouncy ball!")
else:
    print("You win a sticker!")