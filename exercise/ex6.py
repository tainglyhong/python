"""
    Exercise 6 : Basic Conditional logic
    Write a program that perform the action below:
    1. Child (0-12)
    2. teen (13-19)
    3. adult (20-64)
    4. senior (65+)
    
    Ask user to input the age 
    handle the invalid input (negative numbers and non-numeric input)
    use if/elif/else statement
"""

age = input("Enter your age : ")

try:
    age = int(age)
    if age < 0:
        print("Invalid input. Please enter a valid age.")
    elif age <= 12:
        print("You are a child.")
    elif age <= 19:
        print("You are a teenager.")
    elif age <= 64:
        print("You are an adult.")
    else:
        print("You are a senior.")
except ValueError:
    print("Invalid input. Please enter a valid age.")