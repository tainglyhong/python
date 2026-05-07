rental_hours = 2

if rental_hours <= 1:
    print("Enjoy your ride!")
else:
    print("You've used the bike for more than an hour.")
    answer = input("Would you like to continue riding? ")

    if answer == "yes":
        print("Please insert payment.")
    else:
        print("Please return the bike.")