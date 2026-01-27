# inheritance in python 

# Parent class

class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} is working hard.")

# child class
class Develoeper(Employee):
    def __init__(self, name, salary,language):
        super().__init__(name, salary)
        self.language = language

    def code(self):
        print(f"{self.name} is writing {self.language} code!.")


# usage

dev = Develoeper("Alex",90000,"Python")
dev.work() # this comes from parent class
dev.code() # this is unique to the child class