"""
Exercise 10 : shopping cart calculator
write a program that perform the action below:
- show the menu of product with the price
- as the user select what they want the product, quantity
(user can buy multiple time -> loop)
- calculate the total
 - if total > 50 discount 5%
 - if total > 100 discount 10%

what we need to do :
- using the while loop for shopping
- using the nested dictionary for product
"""

product_info = {
    1: {"name": "mouse", "price": 2.50},
    2: {"name": "kayborad", "price": 3.50},
    3: {"name": "stylus pen", "price": 4.50},
}

# print(product_info.items())


def display_menu():
    for item_id, item_info in product_info.items():
        print(f"{item_id}. {item_info['name']} - ${item_info['price']:.2f}")

def calculate_total(cart):
    
    # total = 0
    # for item in cart.values():
    #     total_each_item = item['price'] * item['quantity']
    #     total += total_each_item
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    
    if total > 100:
        discount = 0.1
        discount_message = "10% discount applied."
    elif total > 50:
        discount = 0.05
        discount_message = "5% discount applied."
    else:
        discount = 0
        discount_message = "No discount."
        
    discounted_total = total * (1- discount)
    
    return discounted_total, discount_message
    
    # discounted = total * discount
    # discounted_total = total - discounted
    


def main():
    cart = {}
    while True:
        display_menu()
        try:
            item_number = int(input("Enter your items number : "))
            if item_number not in product_info:
                print("Invalid item number, please try again.")
                continue
        except ValueError:
            print("Invalid input.")
        
        try:
            quantity = int(input("quantity : "))
            if quantity <= 0:
                print("quantity must be greater than zero!")
                continue
        except ValueError:
            print("Invalid input.")
            
        # add item to cart

        item = product_info[item_number]
        
        if item_number in cart:
            cart[item_number]["quantity"] += quantity
        else:
            cart[item_number] = {
                "name" : item["name"], 
                "price" : item["price"], 
                "quantity" : quantity}
        
        while True:
            add_more = input("Add more? (y/n): ").lower().strip()
            
            if add_more in ["y","n","yes","no"]:
                break
            else:
                print("Invalid input.")
                
        if add_more == "n" or add_more == "no":
            break
    
    discounted_total, discount_message = calculate_total(cart=cart)

    print("\nYour cart : ")
    for item in cart.values():
        # print(f"{item["name"]} x {item["quantity"]} = ${item["price"] * {item["quantity"]}}")
        print(f"{item['name']} x {item['quantity']} = ${item['price'] * item['quantity']:.2f}")
        
    
    print(f"\nTotal : ${discounted_total} ({discount_message})")
    
if __name__ == "__main__":
    main()
