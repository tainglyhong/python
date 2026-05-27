correct_username = "admin"
correct_password = "1234"

while True:
    username = input("Username: ")
    password = input("Password: ")

    if username == correct_username and password == correct_password:
        print("Login successful")
        break
    else:
        if username != correct_username:
            print("Wrong username")
        else:
            print("Wrong password")
            
    