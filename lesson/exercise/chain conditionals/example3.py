# What happens if you enter a vehicle name other than "mega cycle" or "mega kart"?
vehicle = input("Pick a vehicle: ")

speed = 5
acceleration = 5

# Players unlock mega vehicles by winning a race on every course.
if vehicle == "mega cycle":
    acceleration = acceleration + 4
elif vehicle == "mega kart":
    speed = speed + 2
    acceleration = acceleration + 2

print(
    "The " + vehicle + " has " + str(speed) + " speed and "
    + str(acceleration) + " acceleration."
)