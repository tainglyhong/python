# NO return value
def display_action_menu(pet_name):
    """Displays the action menu for the user to choose from."""
    print("**** ACTION MENU ****")
    print("1. Feed " + pet_name + ".")
    print("2. Play with " + pet_name + ".")
    # return pet_name

    print("3. Take " + pet_name + " for a walk.")
    print("4. Put " + pet_name + " to bed.")
    print()


display_action_menu("Popple")

empty_result = display_action_menu("Spike")
print(empty_result)