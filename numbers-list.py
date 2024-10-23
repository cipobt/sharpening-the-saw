import random
import math

# ANSI color codes for a colorful menu
RESET = "\033[0m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RED = "\033[31m"

def get_number_list(prompt="Enter numbers separated by spaces: "):
    """Prompts the user for a list of integers and handles invalid input."""
    try:
        return list(map(int, input(prompt).split()))
    except ValueError:
        print(f"{RED}Please enter valid numbers.{RESET}")
        return []

def get_float_list(prompt="Enter numbers separated by spaces: "):
    """Prompts the user for a list of floats and handles invalid input."""
    try:
        return list(map(float, input(prompt).split()))
    except ValueError:
        print(f"{RED}Please enter valid numbers.{RESET}")
        return []

def calculate_sum(numbers):
    """Calculates the sum of a list of numbers."""
    if not numbers:
        return "No numbers entered."
    return sum(numbers)

def sort_list(numbers):
    """Sorts a list of numbers."""
    return sorted(numbers)

def random_number_generator():
    """
    Prompts the user to input a lower and upper bound, then generates
    a random number between the given bounds.
    """
    try:
        lower_bound = int(input("Enter the lower bound: "))
        upper_bound = int(input("Enter the upper bound: "))
        if lower_bound >= upper_bound:
            print(f"{RED}Lower bound must be less than the upper bound.{RESET}")
        else:
            random_num = random.randint(lower_bound, upper_bound)
            print(f"Random number between {lower_bound} and {upper_bound}: {random_num}")
    except ValueError:
        print(f"{RED}Please enter valid integers.{RESET}")

def reverse_list(numbers):
    """Reverses a list of numbers."""
    return numbers[::-1]

def square_numbers(numbers):
    """Squares each number in the list."""
    return [n**2 for n in numbers]

def calculate_average(numbers):
    """Calculates the average of a list of numbers."""
    if not numbers:
        return "No numbers entered."
    return sum(numbers) / len(numbers)

def find_min_max(numbers):
    """Finds the minimum and maximum of a list of numbers."""
    if not numbers:
        return "No numbers entered."
    return min(numbers), max(numbers)

def find_common_elements(list1, list2):
    """Finds common elements between two lists."""
    return list(set(list1) & set(list2))

def second_largest(numbers):
    """Finds the second largest number in a list."""
    unique_numbers = list(set(numbers))  # Remove duplicates
    unique_numbers.sort(reverse=True)  # Sort in descending order
    return unique_numbers[1] if len(unique_numbers) > 1 else "Not enough unique numbers"

def multiply_elements(numbers):
    """Multiplies all elements in a list."""
    return math.prod(numbers)

def count_even_odd(numbers):
    """Counts the number of even and odd numbers in a list."""
    even_count = len([n for n in numbers if n % 2 == 0])
    odd_count = len([n for n in numbers if n % 2 != 0])
    return even_count, odd_count

def find_smallest(numbers):
    """Finds the smallest number in a list."""
    if not numbers:
        return "No numbers entered."
    return min(numbers)

def is_prime(n):
    """Checks if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_difference(numbers):
    return max(numbers) - min(numbers)

import math

def product_of_numbers(numbers):
    return math.prod(numbers)



# Main menu function with options for different tasks
def main_menu():
    while True:
        print(f"\n{BLUE}Number Manipulation Program{RESET}")
        print(f"{YELLOW}1. Calculate sum of numbers{RESET}")
        print(f"{YELLOW}2. Sort a list of numbers{RESET}")
        print(f"{YELLOW}3. Generate a random number{RESET}")
        print(f"{YELLOW}4. Reverse a list{RESET}")
        print(f"{YELLOW}5. Square numbers in a list{RESET}")
        print(f"{YELLOW}6. Calculate the average of numbers{RESET}")
        print(f"{YELLOW}7. Find minimum and maximum of numbers{RESET}")
        print(f"{YELLOW}8. Find common elements between two lists{RESET}")
        print(f"{YELLOW}9. Find second largest number{RESET}")
        print(f"{YELLOW}10. Multiply elements of a list{RESET}")
        print(f"{YELLOW}11. Count even and odd numbers{RESET}")
        print(f"{YELLOW}12. Find smallest number{RESET}")
        print(f"{YELLOW}13. Check if a number is prime{RESET}")
        print(f"{YELLOW}14. Exit{RESET}")

        choice = input(f"{BLUE}Choose an option (1-14): {RESET}")

        if choice == '1':
            numbers = get_number_list()
            print(f"Sum of the numbers: {calculate_sum(numbers)}")

        elif choice == '2':
            numbers = get_number_list()
            print(f"Sorted list: {sort_list(numbers)}")

        elif choice == '3':
            random_number_generator()

        elif choice == '4':
            numbers = get_number_list()
            print(f"Reversed list: {reverse_list(numbers)}")

        elif choice == '5':
            numbers = get_number_list()
            print(f"Squared numbers: {square_numbers(numbers)}")

        elif choice == '6':
            numbers = get_float_list()
            print(f"Average: {calculate_average(numbers)}")

        elif choice == '7':
            numbers = get_number_list()
            min_num, max_num = find_min_max(numbers)
            print(f"Minimum number: {min_num}, Maximum number: {max_num}")

        elif choice == '8':
            list1 = get_number_list("Enter numbers for the first list: ")
            list2 = get_number_list("Enter numbers for the second list: ")
            print(f"Common elements: {find_common_elements(list1, list2)}")

        elif choice == '9':
            numbers = get_number_list()
            print(f"The second largest number is: {second_largest(numbers)}")

        elif choice == '10':
            numbers = get_number_list()
            print(f"Product of all elements: {multiply_elements(numbers)}")

        elif choice == '11':
            numbers = get_number_list()
            evens, odds = count_even_odd(numbers)
            print(f"Even numbers: {evens}, Odd numbers: {odds}")

        elif choice == '12':
            numbers = get_number_list()
            print(f"The smallest number is: {find_smallest(numbers)}")

        elif choice == '13':
            try:
                number = int(input("Enter a number: "))
                if is_prime(number):
                    print(f"{number} is a prime number.")
                else:
                    print(f"{number} is not a prime number.")
            except ValueError:
                print(f"{RED}Please enter a valid integer.{RESET}")

        elif choice == '14':
            print(f"{GREEN}Exiting the program. Goodbye!{RESET}")
            break

        else:
            print(f"{RED}Invalid choice. Please select a valid option from the menu.{RESET}")

# Run the main menu
if __name__ == "__main__":
    main_menu()


try:
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print(f"The difference between the largest and smallest numbers is: {find_difference(numbers)}")
except ValueError:
    print("Please enter valid numbers.")


try:
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print(f"The product of the numbers is: {product_of_numbers(numbers)}")
except ValueError:
    print("Please enter valid numbers.")
