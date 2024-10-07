def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:n]

number = int(input("Enter a number: "))
print(f"The factorial of {number} is {factorial(number)}")

number = int(input("Enter the length of the Fibonacci sequence: "))
if number < 0:
    print("Please enter a positive number")
else:
    print(f"Fibonacci sequence up to {number}: {fibonacci(number)}")
