"""
    Exercise 5: Boolean logic
    Write a program that perform the action below:
    1. Ask user to input the age and membership status (yes or no) for each person
    2. check the condition below:
        - if age > 65 can get 10% discount
        - if a membership can get 5% discount
        - if age > 65 and a membership can get 15% discount
        - if it not inside the condition above, no discount
    3. print out the message that relate to condition above.
"""

try:
    age = int(input("Enter your age : "))
    membership = input("Do you have a membership? (yes/no) : ").strip().lower()

    discount = 0

    if age >= 65 and membership == 'yes':
        discount = 15
        print(f'You are eligible for both the senior and member discount! (15% off)')
    elif age >= 65 and membership != 'yes':
        discount = 10
        print(f'You are eligible for the senior discount! (10% off)')
    elif age < 65 and membership == 'yes':
        discount = 5
        print(f'You are eligible for the member discount! (5% off)')
    else:
        print(f'You are not eligible for any discount. (No discount)')
        
    print(f'Your discount is : {discount}%')
except ValueError:
    print("Invalid input. Please enter a valid age and membership status.")