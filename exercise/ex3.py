# Type conversions
# Temperature converter
"""
Write a program that do the perform the action below:
1. Ask user to input a temperature in Celsius
2. Convert Celsius to Fahrenheit 
3. Convert Celsius to Kelvin
4. Output all of that 3 type of the temperature 

Formula : 
Farenheit = Celsius x (9/5) + 32
Kelvin = Celsius + 273.15
"""

# ask user to input temp
temp = float(input("Enter temperature in Celsius : "))

# convert to farenheit
farenheit_temp = temp * (9/5) + 32

# convert to kelvin 
kelvin_temp = temp + 273.15

print("Temperature conversion : ")
print(f'Temperature in Celsius : {temp:.2f}°C')
print(f'Temperature in Farenheit : {farenheit_temp:.2f}°F')
print(f'Temperature in Kelvin : {kelvin_temp:.2f}K')