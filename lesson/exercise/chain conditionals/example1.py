percent = int(input("Enter quiz score (out of 100): "))

if percent == 100:
    print("Stellar!")
elif percent >= 90:
    print("Excellent work!")
elif percent >= 75:
    print("Nice job!")
elif percent >= 65:
    print("Good.")
else:
    print("Great effort!")
