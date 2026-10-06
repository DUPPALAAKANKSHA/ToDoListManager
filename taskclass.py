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
