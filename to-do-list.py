todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"'{task}' has been added to your to-do list.")

def show_tasks():
    print("\nYour To-Do List:")
    for i, task in enumerate(todo_list, 1):
        print(f"{i}. {task}")

while True:
    task = input("Enter a task to add (or 'done' to stop): ")
    if task.lower() == 'done':
        break
    else:
        add_task(task)

show_tasks()
