def sort_list(numbers):
    return sorted(numbers)

numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(n) for n in numbers]

print(f"Sorted list: {sort_list(numbers)}")
