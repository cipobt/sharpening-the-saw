todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"'{task}' has been added to your to-do list.")

def show_tasks():
    print("\nYour To-Do List:")
    for i, task in enumerate(todo_list, 1):
        print(f"{i}. {task}")

def word_count(sentence):
    words = sentence.split()
    return len(words)

def find_largest_word(sentence):
    words = sentence.split()
    largest_word = max(words, key=len)
    return largest_word

def word_frequency(text):
    words = text.split()
    frequency = {}
    for word in words:
        word = word.lower().strip(".,!?")
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


def convert_to_uppercase(words):
    return [word.upper() for word in words]


def remove_duplicates(numbers):
    return list(set(numbers))


def is_digit(string):
    return string.isdigit()

def first_and_last_element(lst):
    return lst[0], lst[-1]

def contains_number(numbers, target):
    return target in numbers

def is_alpha(string):
    return string.isalpha()





while True:
    task = input("Enter a task to add (or 'done' to stop): ")
    if task.lower() == 'done':
        break
    else:
        add_task(task)

show_tasks()


user_input = input("Enter a sentence or paragraph: ")
print(f"Word count: {word_count(user_input)}")



sentence = input("Enter a sentence: ")
print(f"The largest word is: {find_largest_word(sentence)}")



user_input = input("Enter a sentence or paragraph: ")
frequencies = word_frequency(user_input)

for word, count in frequencies.items():
    print(f"'{word}' appears {count} time(s).")



user_input = input("Enter words separated by spaces: ").split()
print(f"Uppercase words: {convert_to_uppercase(user_input)}")


try:
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print(f"List without duplicates: {remove_duplicates(numbers)}")
except ValueError:
    print("Please enter valid numbers.")


user_input = input("Enter a string: ")
if is_digit(user_input):
    print(f"'{user_input}' is composed of digits.")
else:
    print(f"'{user_input}' is not composed of digits.")


try:
    elements = input("Enter list elements separated by spaces: ").split()
    first, last = first_and_last_element(elements)
    print(f"First element: {first}, Last element: {last}")
except IndexError:
    print("The list must contain at least one element.")



numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
target = int(input("Enter the number to check: "))

if contains_number(numbers, target):
    print(f"{target} is in the list.")
else:
    print(f"{target} is not in the list.")


user_input = input("Enter a string: ")
if is_alpha(user_input):
    print(f"'{user_input}' contains only alphabetic characters.")
else:
    print(f"'{user_input}' contains non-alphabetic characters.")
