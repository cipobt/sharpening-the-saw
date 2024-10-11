def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

try:
    number = int(input("Enter a number to calculate its factorial: "))
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"The factorial of {number} is {factorial(number)}")
except ValueError:
    print("Please enter a valid integer.")
