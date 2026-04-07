# Positional arguments

def greeting(name, age):
    print(f"Hello, {name}! You are {age} years old.")
    
greeting("Alice", 30)  # Positional arguments

# Keyword arguments

greeting(name="Bob", age=25)  # Keyword arguments
greeting(age=40, name="Charlie")  # Keyword arguments can be in any order