class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def introduction(self):
        return f"I'm {self.first_name} {self.last_name}!"

    def sleep(self):
        print("I will sleep for eight hours")

class Student(Person):
    def __init__(self, first_name, last_name, level):
        super().__init__(first_name, last_name)
        self.level = level

    def introduction(self):
        return super().introduction() + f" I'm a {self.level} student."

person = Person("Cyrus", "Olega")
student = Student("John", "Smith", "3rd Year")
print(person.introduction())
print(student.introduction())
person.sleep()
student.sleep()