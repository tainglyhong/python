def get_trip_distance(start, end):
    return end - start

def get_travel_distance(start, detour_distance, end):
    trip_distance = get_trip_distance(start, end)
    return detour_distance + trip_distance

travel_distance = get_travel_distance(4, 3, 7)
print(travel_distance)

# What is the final value of travel_distance before the program terminates?