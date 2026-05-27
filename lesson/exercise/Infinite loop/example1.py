balance = 1000.00

while True:
    print("=== ATM MENU ===")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        print(f"Your balance is ${balance}")

    elif choice == "2":
        amount = float(input("Enter amount: "))
        print(f"You withdrew ${amount}")
        balance = balance - amount
        
    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid option")