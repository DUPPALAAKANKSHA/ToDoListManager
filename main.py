class Task:

    def __init__(self, name):
        self.name = name
        self.status = "Pending"

    # Operator Overloading
    def __str__(self):
        return self.name + " - " + self.status

    def complete(self):
        self.status = "Completed"


# Child Class
class ImportantTask(Task):

    def __init__(self, name):
        super().__init__(name)
        self.priority = "High"

    # Method Overriding
    def __str__(self):
        return self.name + " - " + self.status + " - Priority: " + self.priority


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


# Create To-Do List object
todo = ToDoList()


# Main Menu
while True:

    print("\n================================")
    print("       TO-DO LIST MANAGER")
    print("================================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Exit")
    print("================================")

    choice = input("Enter your choice: ")

    if choice == "1":

        todo.add_task()

    elif choice == "2":

        todo.view_tasks()

    elif choice == "3":

        todo.complete_task()

    elif choice == "4":

        todo.delete_task()

    elif choice == "5":

        todo.search_task()

    elif choice == "6":

        print("Thank you for using To-Do List Manager!")
        break

    else:

        print("Invalid choice. Please try again.")              