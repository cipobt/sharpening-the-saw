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

# Reversing String function
def reverse_string(s):
    return s[::-1]



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
