
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