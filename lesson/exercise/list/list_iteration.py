# FOR LOOP
friends = ['Gara', 'Hanna', 'Sira']
for friend in friends:
    print('Happy new year:', friend)

# WHILE LOOP
grade = [92, 94, 99, 89, 95, 88]
top_mark = 0
index = 0

while index < len(grade):
    if grade[index] >= 90:
        top_mark += 1
    index += 1
print(f"You got {top_mark} top marks!")


top_mark = 0
for i in range(len(grade)):
    if grade[i] >= 90:
        top_mark += 1
print(f"You got {top_mark} top marks!")



fruits = ["apple", "banana", "orange"]
for i in fruits:
    print(i)
    

# SEARCHING
students = ["John", "Sara", "Mike"]
target = "Sara"
found = False

for student in students:
    if student == target:
        found = True

print(found)