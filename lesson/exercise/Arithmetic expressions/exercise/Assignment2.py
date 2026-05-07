cart_total = float(input("Enter cart total: "))
is_vip = input("VIP customer? (yes/no): ").lower()
shipping_coat = float(input("Enter shipping cost: "))

# Discounts
percent_discount = cart_total * 0.15
fixed_discount = 10.00

# Select best discount
discount = max(percent_discount, fixed_discount) 

# VIP extra discount
vip_discount = cart_total * 0.05 * float(is_vip == "yes")

# Final price
final_price = cart_total - discount - vip_discount

shipping = shipping_coat * (final_price <= 100)

# Total
total = final_price + shipping

print("Total to pay: $" + format(round(total, 2), ".2f"))