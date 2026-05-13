"""
1.  If the user has a pet, use the input() function to ask if their pet’s food contains meat.
    If they enter yes, increment footprint by another 10.
    Note:If the user doesn’t have a pet, make sure you don’t ask the follow-up pet food question. Think carefully about your indentation!
    
2.  If the user commutes 0 days a week, don’t ask them the follow-up question about how they commute.
    You’ll need to add a conditional that controls whether the transportation method input() call runs. Test that your program works if you enter 0 commute days.

3.  If the user commutes by bus or train, increment footprint by 4 * days.
    If the user commutes by bike or foot, increment footprint by days.
"""



# footprint = 0

# has_pet = input("Do you have a pet (yes/no)? ")
# if has_pet == "yes":
#     # Pets consume resources like water, litter, and toys. 
#     footprint = footprint + 5

# days = int(input("How many days a week do you commute to school or work? "))
# transport = input("Do you commute by foot, bike, bus, train, or car? ")

# # Different methods of transportation have different environmental impacts.
# if transport == "car":
#     footprint = footprint + (8 * days)

# print("Your environmental footprint score is " + str(footprint) + ".")
