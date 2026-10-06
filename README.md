# ToDoListManager
# ToDoListManager
To Do List Manager
                          
                            
                            PROBLEM OVERVIEW
The To-Do List Manager is a Python-based console application designed to help users manage their daily tasks. It allows users to add, view, complete, delete, and search tasks through a simple menu-driven interface.
                            
                                
                                OBJECTIVE
•	To develop a simple task management application using Python.
•	To demonstrate Object-Oriented Programming concepts.
•	To organize tasks based on their type and status.
•	To provide basic task operations through a user-friendly menu.

                          DESCRIPTION OF PROJECT
                          
Classes Used


•	Task Class
o	The Task class is the parent class.
       It contains:
o	name – Stores the task name.
o	status – Stores the task status, initially set to "Pending".
o	__str__() – Displays the task name and status.
o	complete() – Changes the task status to "Completed".

•	ImportantTask Class
o	The ImportantTask class is the child class of Task.
            It:
o	Inherits properties and methods from Task.
o	Sets the priority as "High".
o	Overrides the __str__() method to display the task priority.


•	ToDoList Class
o	The ToDoList class manages all tasks.
            It contains:
o	tasks – A list used to store task objects.
o	add_task() – Adds normal or important tasks.
o	view_tasks() – Displays all available tasks.
o	complete_task() – Marks a selected task as completed.
o	delete_task() – Removes a selected task.
o	search_task() – Searches for a task by name.


OOP Concepts Used
•	Constructor
__init__() initializes objects with their required attributes.
•	Inheritance
ImportantTask inherits from the Task class.
•	Method Overriding
ImportantTask provides its own version of the __str__() method.
•	Operator Overloading
The __str__() special method is used to define how task objects are represented when printed.
•	Encapsulation
Task-related data and operations are grouped inside classes.
•	Polymorphism
The same __str__() method behaves differently for Task and ImportantTask objects.


                               Functions Used


•	__init__() – Constructor
o	The __init__() method is a special method that is automatically called when an object is created.
o	It is used to initialize the attributes of an object.
o	In Task:
                             def __init__(self, name):
                                   self.name = name
                                   self.status = "Pending"
            Purpose:
o	Stores the task name.
o	Sets the initial task status to Pending.


•	__str__() – String Representation
o	The __str__() method defines how an object should be displayed when it is printed.
o	In Task:
def __str__(self):
      return self.name + " - " + self.status
            Purpose:
o	Displays the task name and status in a readable format.
o	Demonstrates operator overloading / special method usage.


•	complete() – Complete a Task
o	The complete() method changes the status of a task.
o	In Task:
 def complete(self):
       self.status = "Completed"
            Purpose:
o	Changes the task status from Pending to Completed.


•	add_task() – Add a Task
o	The add_task() method allows the user to create a new task.
o	In Task:
def add_task(self):
              Purpose:
o	Takes the task name as input.
o	Checks whether the task name is empty.
o	Allows the user to choose between Normal Task and Important Task.
o	Creates the appropriate object.
o	Adds the task to the task list.


•	view_tasks() – View Tasks
o	The view_tasks() method displays all tasks stored in the list.
o	In Task:
            def view_tasks(self):
            Purpose:
o	Checks whether tasks are available.
o	Displays all tasks with their numbers.
o	Uses __str__() to display task information.

•	complete_task() – Complete Selected Task
o	The complete_task() method allows the user to select a task and mark it as completed.
o	In Task:
                        def complete_task(self):
            Purpose:
o	Displays available tasks.
o	Takes the task number from the user.
o	Validates the task number.
o	Calls the complete() method.
o	Updates the task status.

•	delete_task() – Delete a Task
o	The delete_task() method removes a selected task from the list.
o	In Task:
                       def delete_task(self):
           Purpose:
o	Displays all available tasks.
o	Takes the task number from the user.
o	Removes the selected task using pop().
o	Displays the deleted task name.

•	search_task() – Search for a Task
o	The search_task() method searches for a task using its name.
o	In Task:
def search_task(self):
             Purpose:
o	Takes a search term from the user.
o	Compares it with existing task names.
o	Performs a case-insensitive search using lower().
o	Displays matching tasks.
o	Displays Task not found if there is no match.
