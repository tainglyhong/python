# range(n) will generate a sequence of numbers from 0 to n-1
# range(start, stop, step)

# i = 0 
# while i <= 5:
#     print(i)

# n = 5
# for i in range(n+1):
#     print(i)
    
# for pattern in range(5):
#     print(pattern)
#     print("][][][][][")
#     print("][][][][][")

# ==========================
# for i in range(10, 26, 5):
#     print(i)
    
# TO-while loop
# i = 10 
# while i < 26:
#     print(i)
#     i += 5
# ==========================

# for file in range(10):
#     file_name = f'date_ {file}.txt'
#     print(f'Creating file: {file_name}')
    
# for file in range(1, 11):
#     file_name = f'date_ {file}.txt'
#     print(f'Creating file: {file_name}')
    
# sum = 0    
# n = int(input("Enter a number : "))
# for i in range(n+1):
#     sum = sum + i
# print(sum)

number = int(input("Enter a number : "))
for i in range(1, 11):
    # print(number, "x", i, "=", number * i)
    print(f"{number} x {i} = {number * i}")