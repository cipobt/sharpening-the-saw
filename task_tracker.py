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

if __name__ == "__main__":
    tracker = TaskTracker()
    tracker.add_task("Example Task")
    tracker.show_tasks()
