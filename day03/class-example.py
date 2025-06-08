class Employee:
    """Class representation for employee data"""

    def __init__(self, name, id, role):
        self.name = name
        self.id = id
        self.role = role
        self.tasks = []

        print(f"Employee {name} assigned ID {id} with role {role}")

    def add_work(self, task):
        return self.tasks.append(task)

employee1 = Employee("Richard", "1234", "Writer")
employee2 = Employee("Jelly", "9876", "Developer")

print("Employee 1 role:", employee1.role)
print("Employee 2 role:", employee2.role)

employee1.add_work("create charts")
employee1.add_work("Print documents")
print(employee1.tasks)