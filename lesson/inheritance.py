# Inheritance in Python
# superclass() are parent class
# subclass()   are child class

# example of inheritance


class Animal:
    def __init__(self, name):
        self.name = name

    # overridable method 
    def speak(self):
        return f"{self.name} makes a sound."

# Dog and Cat are subclasses of the Animal class, inheriting its properties and methods.
# Animal is the superclass
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the constructor of the superclass (Animal)
        self.breed = breed
        
    # method overriding
    def speak(self):
        return f"{self.name} barks."
    
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # Call the constructor of the superclass (Animal)
        self.color = color
        
    # method overriding
    def speak(self):
        return f"{self.name} meows."

my_dog = Dog("Buddy", "Golden Retriever")
my_cat = Cat("Whiskers", "Orange")

print(my_dog.name)  # Output: Buddy (inherited from Animal)
print(my_dog.breed)  # Output: Golden Retriever (specific to Dog)
print(my_dog.speak())  # Output: Buddy barks. (overridden method from Dog class)

print(my_cat.name)  # Output: Whiskers (inherited from Animal)
print(my_cat.color)  # Output: Orange (specific to Cat)
print(my_cat.speak())  # Output: Whiskers meows. (overridden method from Cat class)


