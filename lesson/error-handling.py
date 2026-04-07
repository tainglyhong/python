'''Error handling'''

# no error handling
# result = 10 / 0

# print("Hello, world!")

# with error handling

try: # This block will attempt to execute the code that may raise an exception.
    result = 10 / 0
except: # This block will execute if an exception occurs in the try block.
    print("You cannot divide by zero!")
else: # This block will execute only if no exceptions were raised in the try block.
    print("The result is:", result)
finally: # This block will always execute, regardless of whether an exception occurred or not.
    print("This block will always execute.")