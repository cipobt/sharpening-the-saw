# ANSI color codes
RESET = "\033[0m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RED = "\033[31m"


def calculator_menu():
    """Displays the calculator menu and allows the user to perform basic operations."""
    try:
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


def main_menu():
    """Main menu to allow the user to select which function to use."""
    while True:
        print(f"\n{BLUE}Main Menu:{RESET}")
        print(f"{YELLOW}1. Basic Calculator{RESET}")
        print(f"{YELLOW}2. Simple Interest Calculator{RESET}")
        print(f"{YELLOW}3. Tip Calculator{RESET}")
        print(f"{YELLOW}4. Exit{RESET}")

        choice = input(f"{BLUE}Choose an option (1-4): {RESET}")

        if choice == '1':
            calculator_menu()
        elif choice == '2':
            simple_interest_menu()
        elif choice == '3':
            tip_calculator_menu()
        elif choice == '4':
            print(f"{GREEN}Exiting the program. Goodbye!{RESET}")
            break
        else:
            print(f"{RED}Invalid choice. Please select a valid option.{RESET}")




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

def simple_interest_menu():
    """Prompts the user for principal, rate, and time to calculate simple interest."""
    try:
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the interest rate: "))
        time = float(input("Enter the time in years: "))
        interest = simple_interest(principal, rate, time)
        print(f"Simple Interest: {interest:.2f}")
    except ValueError:
        print("Please enter valid numbers.")


def calculate_tip(total, percentage):
    return total * (percentage / 100)

def tip_calculator_menu():
    """Prompts the user for the total bill and tip percentage to calculate the tip."""
    try:
        total_bill = float(input("Enter the total bill amount: "))
        tip_percentage = float(input("Enter the tip percentage: "))
        tip = calculate_tip(total_bill, tip_percentage)
        print(f"Tip amount: {tip:.2f}")
        print(f"Total amount including tip: {total_bill + tip:.2f}")
    except ValueError:
        print("Please enter valid numbers.")


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



try:
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the interest rate: "))
    time = float(input("Enter the time in years: "))
    interest = simple_interest(principal, rate, time)
    print(f"Simple Interest: {interest:.2f}")
except ValueError:
    print("Please enter valid numbers.")




try:
    total_bill = float(input("Enter the total bill amount: "))
    tip_percentage = float(input("Enter the tip percentage: "))
    tip = calculate_tip(total_bill, tip_percentage)
    print(f"Tip amount: {tip:.2f}")
    print(f"Total amount including tip: {total_bill + tip:.2f}")
except ValueError:
    print("Please enter valid numbers.")
