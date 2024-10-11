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

