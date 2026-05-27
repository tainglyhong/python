"""
1. Define a new function called get_time_trophy() 
that takes the number of hours played 
as a parameter and returns the corresponding trophy name.

2. Call the get_time_trophy() function for each of the following four players: 
one with 2 hours played, 
one with 11, 
one with 33, 
and one with 55.

3. Modify the get_time_trophy() function body to include the Humble Hero trophy.
If the number of hours played is between 24 and 49 hours, inclusive, 
then the function should return the string "Humble Hero".
"""

def get_time_trophy(hours_played):

    if hours_played >= 50:
        trophy_name = "Valiant Veteran"
    elif hours_played >= 24 and hours_played <= 49:
        trophy_name = "Humble Hero"
    elif hours_played >= 10:
        trophy_name = "Active Adventurer"
    else:
        trophy_name = "Trainee Traveller"
    return trophy_name

print(get_time_trophy(2))
print(get_time_trophy(11))
print(get_time_trophy(33))
print(get_time_trophy(48))
print(get_time_trophy(55))
