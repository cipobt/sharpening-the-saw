# ANSI color codes
RESET = "\033[0m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RED = "\033[31m"

def celsius_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit.

    Parameters:
    celsius (float): Temperature in Celsius.

    Returns:
    float: Temperature in Fahrenheit.
    """
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius.

    Parameters:
    fahrenheit (float): Temperature in Fahrenheit.

    Returns:
    float: Temperature in Celsius.
    """
    return (fahrenheit - 32) * 5/9

def is_even(number):
    """
    Checks if a number is even.

    Parameters:
    number (int): The number to check.

    Returns:
    bool: True if even, False if odd.
    """
    return number % 2 == 0

def find_max(a, b, c):
    """
    Finds the maximum of three numbers.

    Parameters:
    a (float): First number.
    b (float): Second number.
    c (float): Third number.

    Returns:
    float: The maximum of the three numbers.
    """
    return max(a, b, c)

def temperature_converter():
    """
    Prompts the user to enter a temperature and its unit (Celsius or Fahrenheit),
    and converts the temperature to the opposite unit.
    """
    try:
        temp = float(input(f"{YELLOW}Enter temperature: {RESET}"))
        unit = input(f"{YELLOW}Is this in Celsius or Fahrenheit (C/F)? {RESET}").upper()
        if unit == "C":
            print(f"{GREEN}{temp}°C is {celsius_to_fahrenheit(temp):.2f}°F{RESET}")
        elif unit == "F":
            print(f"{GREEN}{temp}°F is {fahrenheit_to_celsius(temp):.2f}°C{RESET}")
        else:
            print(f"{RED}Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.{RESET}")
    except ValueError:
        print(f"{RED}Please enter a valid temperature.{RESET}")

def even_odd_checker():
    """
    Prompts the user to enter a number and checks whether the number is even or odd.
    """
    try:
        number = int(input(f"{YELLOW}Enter a number: {RESET}"))
        if is_even(number):
            print(f"{GREEN}{number} is even{RESET}")
        else:
            print(f"{GREEN}{number} is odd{RESET}")
    except ValueError:
        print(f"{RED}Please enter a valid number.{RESET}")

def max_of_three_numbers():
    """
    Prompts the user to enter three numbers and finds the maximum among them.
    """
    try:
        num1 = float(input(f"{YELLOW}Enter first number: {RESET}"))
        num2 = float(input(f"{YELLOW}Enter second number: {RESET}"))
        num3 = float(input(f"{YELLOW}Enter third number: {RESET}"))
        print(f"{GREEN}The maximum number is: {find_max(num1, num2, num3)}{RESET}")
    except ValueError:
        print(f"{RED}Please enter valid numbers.{RESET}")

def main_menu():
    """
    Displays the main menu and allows the user to select a function to run.
    The program continues until the user chooses to exit.
    """
    while True:
        print(f"\n{BLUE}Main Menu{RESET}")
        print(f"{YELLOW}1. Temperature Converter{RESET}")
        print(f"{YELLOW}2. Even or Odd Checker{RESET}")
        print(f"{YELLOW}3. Maximum of Three Numbers{RESET}")
        print(f"{YELLOW}4. Exit{RESET}")

        choice = input(f"{BLUE}Choose an option (1-4): {RESET}")

        if choice == '1':
            temperature_converter()
        elif choice == '2':
            even_odd_checker()
        elif choice == '3':
            max_of_three_numbers()
        elif choice == '4':
            print(f"{GREEN}Exiting program. Goodbye!{RESET}")
            break
        else:
            print(f"{RED}Invalid choice. Please select a number between 1 and 4.{RESET}")

if __name__ == "__main__":
    main_menu()
