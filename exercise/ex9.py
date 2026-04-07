"""
Write a program that perform action below:
- check the password 
- the password at least has 8 digits
- at least 1 digit is uppercase
- at least 1 digits is lowercase
- at least 1 digits is a number

what we need to do:
- show the verify message about password that following our condition
- using boolean flags
"""

has_uppercase = False
has_lowercase = False
has_digit = False

password = input("Enter your password: ")

if len(password) >= 8:
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
               
    if not has_uppercase:
        print("Password must contain at least 1 uppercase character.")
    elif not has_lowercase:
        print("Password must contain at least 1 lowercase character.")
    elif not has_digit:
        print("Password must contain at least 1 digit.")
    else:
        print(f"Your password created successfully!")
        print(f"Your password is : {password}")
else:
    print("Password must be at least has 8 characters.")
    
    
