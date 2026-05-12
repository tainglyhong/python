import random

num_cashiers = 1
num_cooks = 2

waiting_to_order = 0
waiting_for_food = 0

# Restaurant is open for 5 hours = 300 minutes
for minute in range(300):

    # Customers arrive every minute and line up to order.
    waiting_to_order = waiting_to_order + random.randint(0, 6)

    # Cashiers take orders.
    new_orders = min(num_cashiers * 3, waiting_to_order)

    # Customers move from waiting_to_order to waiting_for_food.
    waiting_to_order = waiting_to_order - new_orders
    waiting_for_food = waiting_for_food + new_orders

    # Cooks fill orders.
    completed_orders = min(num_cooks, waiting_for_food)

    # Customers leave after receiving food.
    waiting_for_food = waiting_for_food - completed_orders

    # Print status at the end of each minute
    print("Minute", minute + 1)
    print(str(waiting_to_order) + " customers waiting to order.")
    print(str(waiting_for_food) + " customers waiting for food.")
    print()