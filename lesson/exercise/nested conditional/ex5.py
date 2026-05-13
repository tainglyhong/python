inventory = 0

if inventory > 0:
    print("The item is in stock.")
    purchase = input("Purchase item? (yes/no)")

    if purchase == "yes":
        print("Proceeding to checkout.")
    else:
        print("Thank you for browsing.")
else:
    print("This item is currently out of stock.")
    
