while True:
    print("\n=== GAME MENU ===")
    print("1. Start Game")
    print("2. Settings")
    print("3. Quit")

    choice = input("Choose: ")

    if choice == "1":
        print("Game Started!")

    elif choice == "2":
        print("Opening Settings...")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
