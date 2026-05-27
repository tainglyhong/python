# return value function
def add(a, b):
    sum = a + b
    return sum

def sub(a, b):
    subtract = a - b
    return subtract

def multiple(a, b):
    mul = a * b
    return mul

def division(a, b):
    divi = a / b
    return divi

# pass value to arguments and get return value
result = add(5, 3)
sub_result = sub(3, 5)
mul_result = multiple(2, 10)
divi_result = division(10, 2)

print(f"The sum is: {result}")
print(f"The subtract is: {sub_result}")
print(f"The mutiply is: {mul_result}")
print(f"The division is: {divi_result}")

