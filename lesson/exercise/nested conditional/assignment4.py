# Task:
# Modify this program into a smart ATM system using nested conditionals.
#
# Requirements:
# 1. Correct PIN is 1234
# 2. If PIN is correct:
#       - Ask withdrawal amount
#       - If amount is greater than balance:
#             print "Insufficient balance"
#       - Otherwise:
#             - If amount is greater than 500:
#                   print "Daily limit exceeded"
#             - Else:
#                   print "Transaction successful"
# 3. If PIN is incorrect:
#       print "Wrong PIN"

balance = 1000

pin = input("Enter PIN: ")

if pin == "1234":

    amount = float(input("Enter withdrawal amount: "))

    if amount > balance:
        print("Insufficient balance")

    else:

        if amount > 500:
            print("Daily limit exceeded")

        else:
            print("Transaction successful")

else:
    print("Wrong PIN")
