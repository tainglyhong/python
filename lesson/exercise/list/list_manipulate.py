# LIST CONCATENATION
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
[1, 2, 3, 4, 5, 6]
print(a)
[1, 2, 3]

# LIST SLICING
# A slice copies the portion of a list between a start and stop index. 
# Slices copy elements over to a new list; 
# they do not modify the original list.

t = [2, 3, 5, 6, 33, 34, 24, 123]
print(t[1:3])

print(t[5:9])
        
print(t[3:])

print(t[:4])

print(t[:])
# Remember : just like in strings , the second number is “up to but not including”

string = 'banana'
print(string[1:])

