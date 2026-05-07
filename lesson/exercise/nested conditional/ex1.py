password = input("Choose a new password: ")

if len(password) < 8:
    print("Password must have at least 8 character.")
else:
    confirm_password = input("Re-enter password: ")
    if password != confirm_password:
        print("Passwords don't match.")
    else:
        print("Password changed.")
    
