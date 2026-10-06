# To-Do List Class
class ToDoList:

    def __init__(self):
        self.tasks = []

    # Add Task
    def add_task(self):

        name = input("Enter task name: ")

        if name.strip() == "":
            print("Task name cannot be empty.")
            return

        print("\n1. Normal Task")
        print("2. Important Task")

        choice = input("Choose task type: ")

        if choice == "1":
            task = Task(name)
            self.tasks.append(task)
            print("Task added successfully!")

        elif choice == "2":
            task = ImportantTask(name)
            self.tasks.append(task)
            print("Important task added successfully!")

        else:
            print("Invalid choice.")

    # View Tasks
    def view_tasks(self):

        if len(self.tasks) == 0:
            print("\nNo tasks available.")

        else:
            print("\n========== YOUR TASKS ==========")

            for i, task in enumerate(self.tasks, start=1):
                print(i, ".", task)

    # Complete Task
    def complete_task(self):

        self.view_tasks()

        if len(self.tasks) > 0:

            number = int(input("\nEnter task number to complete: "))

            if number >= 1 and number <= len(self.tasks):

                self.tasks[number - 1].complete()

                print("Task completed!")

            else:
                print("Invalid task number.")

    # Delete Task
    def delete_task(self):

        self.view_tasks()

        if len(self.tasks) > 0:

            number = int(input("\nEnter task number to delete: "))

            if number >= 1 and number <= len(self.tasks):

                deleted_task = self.tasks.pop(number - 1)

                print("Deleted task:", deleted_task.name)

            else:
                print("Invalid task number.")

    # Search Task
    def search_task(self):

        search = input("Enter task name to search: ")

        found = False

        for task in self.tasks:

            if search.lower() in task.name.lower():

                print(task)
                found = True

        if found == False:
            print("Task not found.")
