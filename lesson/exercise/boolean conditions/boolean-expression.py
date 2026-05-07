'''
== equal to
!= not equal to
<  less than
<= less than or equal to
>  greater than
>= greater than or equal to
'''
print(-1 == "-1")
username = input("Pick a username: ")

# Usernames must have at least one character.
is_empty = username == "" 
# print("Is your username empty? " + str(is_empty))
print(f"Is your username empty? {is_empty}")

# Your username can't be the same as mine.
is_available = username != "the_real_kim"
print("Is your username available? " + str(is_available))

# The list of usernames is displayed alphabetically.
comes_first = username < "the_real_kim"
print("Does your username come before mine? " + str(comes_first))

# Usernames must have 5 or more characters.
has_min_chars = len(username) >= 5
print("Is your username at least 5 characters long? " + str(has_min_chars))

'''
expression	                    evaluates to
49 > 0	                            True

12.24 <= 12.24	                    True

15 != 15	                        False

2048 < 2048	                        False

"dogs.png" >= "cats.png"	        True

"555 0842" == "5550842"	            False

"NJ" != ""	                        True

-1 == "-1"                          False
'''
