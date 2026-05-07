bounce_height = 56.4

# Stop when the bounce becomes imperceptible.
while bounce_height > 1:
    display_height = round(bounce_height, 2)
    print("The ball is at " + str(display_height) + " cm")

    # The ball loses 30% of its height on each bounce.
    bounce_height = bounce_height * 0.7
