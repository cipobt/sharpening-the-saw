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


def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


def calculate_tip(total, percentage):
    return total * (percentage / 100)



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



principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

print(f"Simple interest: {simple_interest(principal, rate, time)}")




try:
    total_bill = float(input("Enter the total bill amount: "))
    tip_percentage = float(input("Enter the tip percentage: "))
    tip = calculate_tip(total_bill, tip_percentage)
    print(f"Tip amount: {tip:.2f}")
    print(f"Total amount including tip: {total_bill + tip:.2f}")
except ValueError:
    print("Please enter valid numbers.")
