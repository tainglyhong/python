# OOP is a powerful way to structure your code by creating objects that represent real-world things.


class Car:
    # the function in classes are called methods
    # constructor method
    # make, model, year are paramters, and self.make, self.model, self.year are attributes of the object.
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
        self.color = "Red" # Default color attribute for all cars
    
    def display_info(self):
        print(f"{self.make} {self.model} {self.year}")


# creating an object
car1 = Car("Mazda", "Rx-7", 1992)
car2 = Car("Mazda", "MX-5", 1992)

# print(type(car1))  
car1.display_info()  # Output: 1992 Mazda Rx-7
car2.display_info()  # Output: 1992 Mazda MX-5


# attribute access
print(car1.make)  # Output: Mazda
print(car1.model)  # Output: Rx-7
print(car1.year)  # Output: 1992
print(f'Color of car1: {car1.color}')  # Output: Color of car1: Red
print(f'Color of car2: {car2.color}')  # Output: Color of car2: Red