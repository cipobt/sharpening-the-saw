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

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100




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


principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

print(f"Simple interest: {simple_interest(principal, rate, time)}")
