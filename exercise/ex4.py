""" 
Basic Arithmetic : Shopping Calculator

Write a program that perform the action below:
1. Ask user to input the price of 3 items
2. calculate the subtotal before tax
3. add 8% tax to the subtotal
4. discount 10% if the subtotal more than 50
5. print out all the price of each item, subtotal, tax, discount and total

"""

# ask user to input price of 3 items
item1 = float(input("Enter price of item 1 : $"))
item2 = float(input("Enter price of item 2 : $"))
item3 = float(input("Enter price of item 3 : $"))

# calculate subtotal
subtotal = item1 + item2 + item3

tax = subtotal * 0.08

total_with_tax = subtotal + tax

discount = 0

discount = total_with_tax * 10 / 100 if total_with_tax > 50 else 0

total = total_with_tax - discount


print(f'Price of item 1 : ${item1:.2f}')
print(f'Price of item 2 : ${item2:.2f}')
print(f'Price of item 3 : ${item3:.2f}')
print(f'Subtotal : ${subtotal:.2f}')
print(f'Tax (8%) : ${tax:.2f}')
if discount > 0:
    print(f'Discount (10%) : -${discount:.2f}')
else:
    print('No discount applied')
    
print(f'Total : ${total:.2f}')
