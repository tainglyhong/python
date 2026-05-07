"""Summary of the program:

- Ask if the user has a pet. If yes, ask if the pet's food contains meat:
    - If meat, add 10 to footprint. All pets add 5.
- Ask how many days per week the user commutes.
    - If days == 0, skip asking about transport method.
    - Otherwise ask transport method (convert to lowercase) and add to footprint:
        - car: add 8 * days
        - bus or train: add 4 * days
        - bike or foot: add 1 * days
- Print the final footprint score.
"""

footprint = 0

has_pet = input("Do you have a pet (yes/no)? ")
if has_pet == "yes":
    # Pets consume resources like water, litter, and toys. 
    has_meat = input("Did your pet's food contain meat (yes/no)? ")
    if has_meat == "yes":
        footprint += 10
    footprint = footprint + 5

days = int(input("How many days a week do you commute to school or work? "))
if days > 0:
    transport = input("Do you commute by foot, bike, bus, train, or car? ")
    transport = transport.lower()
    
    # Different methods of transportation have different environmental impacts.
    if transport == "car":
        footprint = footprint + (8 * days)
    elif transport == "bus" or transport == "train":
        footprint = footprint + (4 * days)
    elif transport == "bike" or transport == "foot": 
        footprint = footprint + days

print("Your environmental footprint score is " + str(footprint) + ".")
