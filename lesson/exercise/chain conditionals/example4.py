# Enter a sale price of 40, 60, and then 100. Which branches execute on each run?
purchase_price = 42.70
sale_price = float(input("How much did you sell for? "))

price_diff = round(abs(sale_price - purchase_price), 2)
if price_diff > purchase_price:
    print("There was a huge change in value.")
    
elif price_diff < purchase_price / 10:
    print("There was very little change in value.")

if purchase_price <= sale_price:
    print("You made a profit of $" + str(price_diff))
else:
    print("You had a loss of $" + str(price_diff))