# password = input("Choose a new password: ")

# if len(password) < 8:
#     print("Password must have at least 8 character.")
# else:
#     confirm_password = input("Re-enter password: ")
#     if password != confirm_password:
#         print("Passwords don't match.")
#     else:
#         print("Password changed.")


answer = ""
quest_complete = True

if answer == "west":
    print("You see a dark forest.")
    
else:
    if quest_complete:
        print("You should head to the forest.")
    print("You arrive at home.")


"""
Question
When the output show "You see a dark forest"   ? when answer == "west"
When the output show "You should head to the forest./You arrive at home." ? when answer is false and quest_complete = True
When the output show "You arrive at home." when answer is false and quest_complete = False
When the output show "You should head to the forest." Not possible
"""
