username = ""

# Keep prompting until the user enters a valid username.
while len(username) < 5:
    print("Usernames must be at least 5 characters.")
    username = input("Choose a username: ")

print("Username changed.")
