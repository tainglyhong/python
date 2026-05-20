# Hybrid Vehicle Code
import random

battery = random.randint(1, 5)
print("Starting at " + str(battery) + " battery.")

gas_tank = random.randint(1, 5)
print("Starting at " + str(gas_tank) + " gas.")

# Hybrid vehicles can use either battery or gas power.
while battery > 0 or gas_tank > 0:

    # Prefer battery to gas, if the charge is high.
    if battery > gas_tank:
        print("Battery!")
        battery = battery - 1
    else:
        print("Gas!")
        gas_tank = gas_tank - 1
