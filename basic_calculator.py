def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

print("Simple Calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")

if operation == "+":
    print(f"Result: {add(num1, num2)}")
elif operation == "-":
    print(f"Result: {subtract(num1, num2)}")
elif operation == "*":
    print(f"Result: {multiply(num1, num2)}")
elif operation == "/":
    print(f"Result: {divide(num1, num2)}")
else:
    print("Invalid operation")
