# TODO: Add support for Saturn (9), Uranus (8.7), and Neptune (11).
planet = input("Pick a planet: Mars, Mercury, Venus, or Jupiter? ")

# We measure a planet's gravitational force in m/s^2.
gravity = 0.0

if planet == "Mars" or planet == "Mercury":
    gravity = 3.7
elif planet == "Venus":
    gravity = 8.9
elif planet == "Jupiter":
    gravity = 23.1
else:
    print("Unrecognized planet.")

if gravity:
    earth_weight = float(input("How much does it weigh on Earth (kg)? "))

    # An object's weight = mass * gravity.
    earth_gravity = 9.81
    mass = earth_weight / earth_gravity
    new_weight = round(mass * gravity, 1)

    print("It would weight " + str(new_weight) + " kg on " + planet + ".")