# range is a built-in function that generates a sequence of numbers
# sequence of numbers is from 0 to n-1, where n is the argument passed to range
# range(n) = 0 to n-1
# range(5) = 0, 1, 2, 3, 4 (n = 5, 5-1 = 4)

for number in range(5):
    if number == 3:
        break
    print(f"Number: {number}")