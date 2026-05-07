# If the user enters the wrong data type, print the message: The correct answer is float.
# If the user enters the wrong length, print the message: The correct answer is 2.
# If the user answers integer for the first question, print the message: Integers can't have decimals.
"""
Add a new variable score at the top of the program.
Any time the user answers a question correctly, increment the score variable by one.
At the end of the program, print the value of score.
"""
score = 0

answer = input("What data type is the value 6.3? ")

if answer == "float":
    print("You got it!")
    score = score + 1
elif answer == "integer":
    print("Integers can't have decimals.")
else:
    print("The answer is float.")

answer = int(input("What does len(\"hi\") evaluate to? "))
if answer == 2:
    print("You got it!")
    score = score + 1
    
else:
    print("The correct answer is 2.")

print("The score is : " + str(score))