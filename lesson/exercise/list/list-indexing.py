colors = ['red', 'green', 'blue', 'black', 'white']

# Access the list by element of a list by index
# An index refers to a specific position in the list, starting at index 0 like array

print(colors[0])
print(colors[3])
print(colors[4])
# print(colors[9]) #error : because list index out of range

# how to know the range of list
print(len(colors)) # 5 : mean it's count the element in the list

# Negative index
print(colors[-1]) #count reverse from the last, starting at index -1 (index 4)
print(colors[-3])
print(colors[-5])

# List are mutable = mean can be change or changable
# string are immutable = mean cannot be change

# x = 'banana'
# x[0] = 'B'
# print(x) # It would be error, but

x = ['banana', 'apple']
print(x[0])
x[0] = 'Banana'
print(x[0])
