# we can also put a tuple on the 
# left-hand side of an assignment statement

(x, y) = (4, 'fred')
print(y)

(a, b) = (99, 98)
print(a)

# Tuples are comparable
t = (0, 1, 2) < (5, 1, 2)
print(t)

t = (0, 1, 2000) < (0, 1, 200)
print(t)

