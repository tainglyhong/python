# Tuples are like Lists
# Tuple are another kind of sequence that function much like a list
# - they have elements which are indexed starting at 0

x = ('Glenn', 'Sally', 'Joseph')
print(x[2])

y = (1, 9, 2)
print(y)
print(max(y))

for iter in y:
    print(iter)
    
# Tuple are immutable
z = (2, 5, 6)
# z[0] = 3
print(z)

# Things you can not to do with tuple like sort(), append(), reverse() .....
# you can check what you can do with tuple
t = tuple()
print(dir(t))