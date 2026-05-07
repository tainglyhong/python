# function is a block of code that performs a specific task

# defining a function
def function_name():
    print("This is a function 1")
    print("This is a function 2")
    print("This is a function 3")
    

# calling the function
function_name()

# function with auguments
def greet(name):
    print(f"Hello, {name}!")
    
greet("Alice")


# return value function
def add(a, b):
    return a + b

# pass value to arguments and get return value
result = add(5, 3)
print(f"The sum is: {result}")

# default argument value
def greeting(name = "Guest"):
    print(f"Hello, {name}!")
    
greeting()  # uses default value

