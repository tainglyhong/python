# break mean terminate the loop
# continue mean skip the loop

# for i in range(5):
#     if i == 3:
#         break
#     print(i)

# for i in range(5):
#     if i == 2:
#         continue
#     print(i)


    
password = "1234567"

for attempt in range(2):
    guess = input("Enter password: ")

    if guess == password:
        print("Welcome back!")
        break

    print("Incorrect password.")

print("Program exiting.")


# total_people = 0

# while total_people < 20:
#     group_size = int(input("How many people? "))

#     # TODO: Add a comment here.
#     if group_size > 4:
#         continue

#     total_people = group_size + total_people

# print(total_people)


# The school wants every ID number to be 7 digits long, 
# but it does not want ID numbers to contain the digit 4.

# import random

# student_id = ""
# digit = 0

# while len(student_id) < 7:
#     # TODO: Don't allow 4 as a digit.
#     digit = random.randint(1, 9)
#     if digit == 4:
#         continue
    
#     student_id = student_id + str(digit)

# print("Your student ID is: " + student_id)