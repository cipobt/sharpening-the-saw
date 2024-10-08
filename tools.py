def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def is_even(number):
    return number % 2 == 0





temp = float(input("Enter temperature: "))
unit = input("Is this in Celsius or Fahrenheit (C/F)? ").upper()

if unit == "C":
    print(f"{temp}°C is {celsius_to_fahrenheit(temp):.2f}°F")
elif unit == "F":
    print(f"{temp}°F is {fahrenheit_to_celsius(temp):.2f}°C")
else:
    print("Invalid input")


number = int(input("Enter a number: "))
if is_even(number):
    print(f"{number} is even")
else:
    print(f"{number} is odd")
