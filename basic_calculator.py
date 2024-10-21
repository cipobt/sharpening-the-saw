import math

# ANSI color codes for a colorful menu
RESET = "\033[0m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RED = "\033[31m"


def add(a, b):
    """
    Adds two numbers.

    Parameters:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of the two numbers.
    """
    return a + b


def subtract(a, b):
    """
    Subtracts the second number from the first number.

    Parameters:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The result of subtracting b from a.
    """
    return a - b


def multiply(a, b):
    """
    Multiplies two numbers.

    Parameters:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of the two numbers.
    """
    return a * b


def divide(a, b):
    """
    Divides the first number by the second number.

    Parameters:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The result of the division if b is not zero, otherwise an error message.
    """
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def simple_interest(principal, rate, time):
    """
    Calculates simple interest.

    Parameters:
        principal (float): The principal amount.
        rate (float): The rate of interest (percentage).
        time (float): The time in years.

    Returns:
        float: The calculated simple interest.
    """
    return (principal * rate * time) / 100


def calculate_tip(total, percentage):
    """
    Calculates the tip based on the total bill and tip percentage.

    Parameters:
        total (float): The total bill amount.
        percentage (float): The tip percentage.

    Returns:
        float: The calculated tip amount.
    """
    return total * (percentage / 100)


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
            print(f"{RED}Invalid operation. Please choose from +, -, *, or /.{RESET}")
    except ValueError:
        print(f"{RED}Please enter valid numbers.{RESET}")


def simple_interest_menu():
    """Prompts the user for principal, rate, and time to calculate simple interest."""
    try:
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the interest rate: "))
        time = float(input("Enter the time in years: "))
        interest = simple_interest(principal, rate, time)
        print(f"Simple Interest: {interest:.2f}")
    except ValueError:
        print(f"{RED}Please enter valid numbers.{RESET}")


def tip_calculator_menu():
    """Prompts the user for the total bill and tip percentage to calculate the tip."""
    try:
        total_bill = float(input("Enter the total bill amount: "))
        tip_percentage = float(input("Enter the tip percentage: "))
        tip = calculate_tip(total_bill, tip_percentage)
        print(f"Tip amount: {tip:.2f}")
        print(f"Total amount including tip: {total_bill + tip:.2f}")
    except ValueError:
        print(f"{RED}Please enter valid numbers.{RESET}")


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


# Run the main menu
if __name__ == "__main__":
    main_menu()
