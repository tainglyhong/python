abc = 'with three words'
stuff = abc.split()

print(stuff)
print(len(stuff))

print(stuff[0])

# for w in stuff:
#     print(w)

line = 'A lot           of spaces'

etc = line.split()
print(etc)
print(len(etc))

line = 'first;second;third'
thing = line.split()
print(thing)
print(len(thing))

thing = line.split(';')
print(thing)

print(list(range(5)))