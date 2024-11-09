class Task:
    def __init__(self, title, priority="Normal"):
        self.title = title
        self.completed = False
        self.priority = priority


    def mark_completed(self):
        self.completed = True

class TaskTracker:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, priority="Normal"):
        new_task = Task(title, priority)
        self.tasks.append(new_task)
        print(f"Task '{title}' with priority '{priority}' added!")


    def show_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
        else:
            sorted_tasks = sorted(self.tasks, key=lambda x: x.priority)
            print("\nTasks:")
            for idx, task in enumerate(sorted_tasks, 1):
                status = "Completed" if task.completed else "Pending"
                print(f"{idx}. {task.title} [{status}] - Priority: {task.priority}")


    def mark_task_completed(self, index):
        try:
            self.tasks[index - 1].mark_completed()
            print(f"Task '{self.tasks[index - 1].title}' marked as completed.")
        except IndexError:
            print("Invalid task number.")

    def delete_task(self, index):
        try:
            task = self.tasks.pop(index - 1)
            print(f"Task '{task.title}' deleted.")
        except IndexError:
            print("Invalid task number.")

def display_menu():
    print("\nTask Tracker Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")



if __name__ == "__main__":
    tracker = TaskTracker()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            tracker.add_task(title)
        elif choice == "2":
            tracker.show_tasks()
        elif choice == "3":
            index = int(input("Enter task number to mark as completed: "))
            tracker.mark_task_completed(index)
        elif choice == "4":
            index = int(input("Enter task number to delete: "))
            tracker.delete_task(index)
        elif choice == "5":
            print("Exiting Task Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")
