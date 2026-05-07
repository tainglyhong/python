# Add a conditional that sets waste_type to the value "recycling" 
# if the item is plastic.

# Set waste_type to the value "trash" 
# if a plastic item is smaller than 7.5 cm.


material = input("What material is it? ")
length = float(input("What is its length in cm? "))

waste_type = ""

if material == "plastic":
    waste_type = "recycling"
    
if length < 7.5:
    waste_type = "trash"

print("Please deposit your item in the " + waste_type + " bin.")
