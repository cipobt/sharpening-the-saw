def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def is_even(number):
    return number % 2 == 0

def find_max(a, b, c):
    return max(a, b, c)

def temperature_converter():
    try:
        temp = float(input("Enter temperature: "))
        unit = input("Is this in Celsius or Fahrenheit (C/F)? ").upper()
        if unit == "C":
            print(f"{temp}°C is {celsius_to_fahrenheit(temp):.2f}°F")
        elif unit == "F":
            print(f"{temp}°F is {fahrenheit_to_celsius(temp):.2f}°C")
        else:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Please enter a valid temperature.")

def even_odd_checker():
    try:
        number = int(input("Enter a number: "))
        if is_even(number):
            print(f"{number} is even")
        else:
            print(f"{number} is odd")
    except ValueError:
        print("Please enter a valid number.")

def max_of_three_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        print(f"The maximum number is: {find_max(num1, num2, num3)}")
    except ValueError:
        print("Please enter valid numbers.")

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Temperature Converter")
        print("2. Even or Odd Checker")
        print("3. Maximum of Three Numbers")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            temperature_converter()
        elif choice == '2':
            even_odd_checker()
        elif choice == '3':
            max_of_three_numbers()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main_menu()
