class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_completed(self):
        self.completed = True

class TaskTracker:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        new_task = Task(title)
        self.tasks.append(new_task)
        print(f"Task '{title}' added!")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
        else:
            print("\nTasks:")
            for idx, task in enumerate(self.tasks, 1):
                status = "Completed" if task.completed else "Pending"
                print(f"{idx}. {task.title} [{status}]")

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
    tracker.add_task("Example Task")
    tracker.show_tasks()
