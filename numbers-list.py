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

def calculate_average(numbers):
    return sum(numbers) / len(numbers)


try:
    numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
    if numbers:
        print(f"Average: {calculate_average(numbers)}")
    else:
        print("No numbers entered.")
except ValueError:
    print("Please enter valid numbers.")

