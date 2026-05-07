"""
1. Identify and add the two missing type conversions such that the program
runs without error

2. use build-in function round() the final price to two decimal places.
example : round(3.141592) -> 3.14

3. Add a new input() prompt that asks the user to enter a shipping cost.

4. Add the entered shipping cost to the final price.
"""

base_price = input("Enter cart total: ")

# Available coupon codes include 15% off and $12 off.
percent_discount = base_price - base_price * .15
fixed_discount = base_price - 12

# Pick the coupon that offers the best discount.
final_price = min(fixed_discount, percent_discount)
print("Your best price is $" + final_price)