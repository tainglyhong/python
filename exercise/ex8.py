"""
Exercise 8 : List analysis
write a program that perform the action below:
- ask user to input a 5 numbers
- store the numbers in a list
- define a even number in the list and print the even numbers
- sum of the odd number in the list and print the sum
what we need to do:
- use for loop to process the list
- using a modulo operator (%) to determine if a number is even or odd
"""

num_lists = []

num = list(map(int, input("Enter 5 numbers: ").split()))[:5]


even_numbers = []
odd_sum = 0

for num in num_lists:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_sum += num


print("Even numbers in the list:", even_numbers)
print("Sum of odd numbers in the list:", odd_sum)