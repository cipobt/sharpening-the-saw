import random

def guessing_game():
    target_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            if guess < target_number:
                print("Too low!")
            elif guess > target_number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers_in_range(start, end):
    primes = [n for n in range(start, end + 1) if is_prime(n)]
    return primes

def sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(number)))


def check_number_sign(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"




guessing_game()


try:
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    print(f"Prime numbers between {start} and {end}: {prime_numbers_in_range(start, end)}")
except ValueError:
    print("Please enter valid integers.")


try:
    user_input = int(input("Enter a number: "))
    print(f"Sum of digits: {sum_of_digits(user_input)}")
except ValueError:
    print("Please enter a valid integer.")


try:
    user_input = float(input("Enter a number: "))
    print(f"The number is {check_number_sign(user_input)}.")
except ValueError:
    print("Please enter a valid number.")
