# Dictionary - A linear collection of key-value pairs look up by ‘tag’ or ‘key’
# Dictionary literals use curly braces and have a list of key : value pair

inventory = {'orange' : 12, 'apple' : 34, 'banana' : 3}
print(inventory)

# empty dictionay
ooo = {}
print(ooo)

cabinet = dict()
cabinet['summer'] = 12
cabinet['fall'] = 3
cabinet['spring'] = 75

print(cabinet)
print(cabinet['fall'])

cabinet['fall'] = cabinet['fall'] + 2
print(cabinet)

# loop dictionaries
for key in cabinet:
    print(key, cabinet[key])
    
inventory = {'orange' : 12, 'apple' : 34, 'banana' : 3}
print(list(inventory))
print(list(inventory.keys()))
print(list(inventory.values()))
print(list(inventory.items()))

for key, value in inventory.items():
    print(key, value)