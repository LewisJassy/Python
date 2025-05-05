# This is where a sub-class acquires properties and behaivours from a parent class

# First implement a parent class
class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

# Implement a sub-class that will inherit from the parent class
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")

if __name__ == "__main__":
    dog = Dog("Tom")
    dog.bark()
    dog.eat()

# Real-World example
class Employee:
    def __init__(self,salary, name):
        self.name = name
        self.salary = salary

    def employee_name(self):
        print(f"Emplyee name: {self.name}, Employee salary: {self.salary}")

class Manager(Employee):
    def __init__(self, salary, name, bonus):
        super().__init__(salary,name)
        self.bonus = bonus

    def employee_bonus(self):
        print(f"Bonus: {self.bonus}")

if __name__ == "__main__":
    employee_rappo = Manager(70000, "Lewis Njaci", 10000)
    employee_rappo.employee_name()
    employee_rappo.employee_bonus()
