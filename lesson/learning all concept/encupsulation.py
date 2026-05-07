'''

'''

class Person:
    def __init__(self, name, age):
        self.name = name # public
        self.__age = age # private
        
    def get_age(self):
        return self.__age
        
person1 = Person("Alice", 30)
print(person1.name)  # Output: Alice
# print(person1._Person__age)  # Output: 30
print(person1.get_age())  # Output: 30