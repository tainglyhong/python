import random

def calculate_total(price, quantity):
    return price * quantity

def generate_seat():
    return random.randint(1, 100)

while True:

    print("\n==============================")
    print("   MOVIE TICKET SYSTEM")
    print("==============================")
    print("1. Book Ticket")
    print("2. Exit")

    choice = input("Choose an option: ")

    if choice == "2":
        print("\nThank you for using the system.")
        break

    if choice != "1":
        print("Invalid option!")
        continue

    print("\n===== CUSTOMER INFORMATION =====")

    name = input("Enter customer name: ")
    age = int(input("Enter age: "))

    # Movie Selection
    print("\n===== MOVIE LIST =====")
    print("1. Avengers")
    print("2. Kung Fu Panda")
    print("3. Inside Out")

    movie = int(input("Choose Movie (1-3): "))

    # Validate Movie
    if movie < 1 or movie > 3:
        print("Invalid movie selection!")
        continue

    # Determine Movie Name
    if movie == 1:
        movie_name = "Avengers"
    elif movie == 2:
        movie_name = "Kung Fu Panda"
    else:
        movie_name = "Inside Out"

    # Age Restriction
    if movie == 1:
        if age < 13:
            print("\nAccess Denied!")
            print("Avengers requires age 13 or above.")
            continue

    # Ticket Quantity
    quantity = int(input("Number of tickets: "))

    ticket_price = 5

    total = calculate_total(ticket_price, quantity)

    # Age Discount
    discount = 0

    if age < 12:
        discount = total * 0.50

    elif age >= 60:
        discount = total * 0.30

    total = total - discount

    # VIP Member
    vip = input("VIP Member (yes/no): ")

    if vip.lower() == "yes" and quantity > 3:

        vip_discount = total * 0.10
        total = total - vip_discount

    # Generate Seat Number
    seat_number = generate_seat()

    # Receipt
    print("\n==============================")
    print("       BOOKING RECEIPT")
    print("==============================")

    print("Customer Name :", name)
    print("Age           :", age)
    print("Movie         :", movie_name)
    print("Tickets       :", quantity)
    print("Seat Number   :", seat_number)

    print("Total Cost    : $", round(total, 2))

    # Nested Conditional
    if vip.lower() == "yes":

        print("\nVIP Customer")

        if quantity > 5:
            print("Reward : Free Popcorn")
        else:
            print("Reward : Free Drink")

    else:
        print("\nRegular Customer")

    print("\nBooking Successful!")
    
