"""
    String manipulation exercises.
    Write a program that perform the action below:
    1. Ask user to input a first name and last name, by using 2 input() function.
    2. concate the first name and last name together as a full name
    3. convert the full name to the title case
    4. count the characters of the full name. Note : space not counted.
    5. create a nickname  and concat it with 
    first 3 character of the first name and 2 last character of last name 
    and convert the nickname to the title case.
    
"""

first_name = input("Enter your first name : ").strip() # strip() is used to remove leading and trailing whitespace from the input string.
last_name = input("Enter your last name : ").strip()

full_name = f'{first_name} {last_name}'
full_name_title = full_name.title()

length = len(full_name.replace(" ", ""))

nickname = f'{first_name[:3]}{last_name[-2:]}'.lower()


print(f'Full name : {full_name}')
print(f'Full name in title case : {full_name_title}')
print(f'Number of characters in full name : {length} (excluding space)')
# print(f'firstname : {first_name[:3]}')
# print(f'lastname : {last_name[-2:]}')
print(f'Nickname : {nickname}')