n = 10
# while n > 0:
#     print("N Minus and counting " + str(n))
#     n -= 1

# for i in range(10, 0, -1):
#     if i == 3:
#         continue
#     print("N minus and counting " + str(i))


# for number in range(5):
#     if number == 2:
#         continue
#     print(f"Number: {number}")


number = int(input("Enter a number : "))
for i in range(11):
    total = number * i
    print(f"{number} * {i} = {total}")