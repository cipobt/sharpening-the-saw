import random

def calculate_sum(numbers):
    return sum(numbers)

def sort_list(numbers):
    return sorted(numbers)

def random_number_generator():
    try:
        lower_bound = int(input("Enter the lower bound: "))
        upper_bound = int(input("Enter the upper bound: "))
        if lower_bound >= upper_bound:
            print("Lower bound must be less than the upper bound.")
        else:
            random_num = random.randint(lower_bound, upper_bound)
            print(f"Random number between {lower_bound} and {upper_bound}: {random_num}")
    except ValueError:
        print("Please enter valid integers.")

def reverse_list(numbers):
    return numbers[::-1]

def square_numbers(numbers):
    return [n**2 for n in numbers]

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def find_min_max(numbers):
    return min(numbers), max(numbers)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def second_largest(numbers):
    unique_numbers = list(set(numbers))  # Remove duplicates
    unique_numbers.sort(reverse=True)  # Sort in descending order
    return unique_numbers[1] if len(unique_numbers) > 1 else "Not enough unique numbers"

def convert_to_integers(strings):
    return [int(num) for num in strings]

import math

def multiply_elements(numbers):
    return math.prod(numbers)




numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(n) for n in numbers]

print(f"Sorted list: {sort_list(numbers)}")


random_number_generator()


numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(n) for n in numbers]

print(f"The sum of the numbers is: {calculate_sum(numbers)}")


numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(n) for n in numbers]

print(f"Reversed list: {reverse_list(numbers)}")


try:
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print(f"Squared numbers: {square_numbers(numbers)}")
except ValueError:
    print("Please enter valid numbers.")



try:
    numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
    if numbers:
        print(f"Average: {calculate_average(numbers)}")
    else:
        print("No numbers entered.")
except ValueError:
    print("Please enter valid numbers.")


try:
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    min_num, max_num = find_min_max(numbers)
    print(f"Minimum number: {min_num}")
    print(f"Maximum number: {max_num}")
except ValueError:
    print("Please enter valid numbers.")


try:
    list1 = list(map(int, input("Enter numbers for the first list separated by spaces: ").split()))
    list2 = list(map(int, input("Enter numbers for the second list separated by spaces: ").split()))
    common_elements = find_common_elements(list1, list2)
    print(f"Common elements: {common_elements}")
except ValueError:
    print("Please enter valid numbers.")



try:
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print(f"The second largest number is: {second_largest(numbers)}")
except ValueError:
    print("Please enter valid numbers.")


user_input = input("Enter numbers separated by spaces: ").split()
try:
    numbers = convert_to_integers(user_input)
    print(f"Converted list: {numbers}")
except ValueError:
    print("Please enter valid numbers.")

try:
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print(f"The product of all elements is: {multiply_elements(numbers)}")
except ValueError:
    print("Please enter valid numbers.")
