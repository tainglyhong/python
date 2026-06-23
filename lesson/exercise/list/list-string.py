# SPLIT
abc = 'with three words'
stuff = abc.split()
print(stuff)
print(len(stuff))

print(stuff[0])

for w in stuff:
    print(w)


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

# RANGE TO LIST
print(list(range(5)))

# JOIN
words = ["I", "Love", "Python", "so", "much"]
sentence = " ".join(words)
print(sentence)