# Factorial function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Fibonacci function
def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:n]

# Prime Checker function
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

try:
    value = float(input("Enter the distance: "))
    unit = input("Is the distance in kilometers or miles? (K/M): ").upper()

    if unit == 'K':
        print(f"{value} kilometers is equal to {km_to_miles(value):.2f} miles.")
    elif unit == 'M':
        print(f"{value} miles is equal to {miles_to_km(value):.2f} kilometers.")
    else:
        print("Invalid unit. Please enter 'K' for kilometers or 'M' for miles.")
except ValueError:
    print("Please enter a valid number.")



number = int(input("Enter a number: "))
print(f"The factorial of {number} is {factorial(number)}")


number = int(input("Enter the length of the Fibonacci sequence: "))
if number < 0:
    print("Please enter a positive number")
else:
    print(f"Fibonacci sequence up to {number}: {fibonacci(number)}")


number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")


user_string = input("Enter a string: ")
print(f"Reversed string: {reverse_string(user_string)}")


user_string = input("Enter a word or phrase: ")
if is_palindrome(user_string):
    print(f"'{user_string}' is a palindrome")
else:
    print(f"'{user_string}' is not a palindrome")
