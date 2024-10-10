import random

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


numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(n) for n in numbers]

print(f"Sorted list: {sort_list(numbers)}")


random_number_generator()
