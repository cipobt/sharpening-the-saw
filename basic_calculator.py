def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

try:
    print("Basic calculator")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ")

    if operation == '+':
        print(f"Result: {add(num1, num2)}")
    elif operation == '-':
        print(f"Result: {subtract(num1, num2)}")
    elif operation == '*':
        print(f"Result: {multiply(num1, num2)}")
    elif operation == '/':
        print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid operation. Please choose from +, -, *, or /.")
except ValueError:
    print("Please enter valid numbers.")


def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

print(f"Simple interest: {simple_interest(principal, rate, time)}")
