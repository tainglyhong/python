"""
When the computer reaches a return statement, 
it immediately exits out of the function and returns execution 
to the caller. That means any remaining lines of code inside 
the function body don't execute!
"""
def get_greeting(days_since_spoken):
    """Returns a greeting based on the character's last interaction."""
    if days_since_spoken < 1:
        return "Oh, it's you again."
        print("I AM UNREACHABLE!")
    else:
        return "Always good to see you."
        print("I AM UNREACHABLE!")

    print("I AM UNREACHABLE!")
    return "Nice to meet you."


print(get_greeting(0))
print(get_greeting(4))
print(get_greeting(100))
