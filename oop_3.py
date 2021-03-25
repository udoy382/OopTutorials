# class Methods In Python @classmethod

class Employee:
    increment = 1.5
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.increment = 1.4
    
    def increase(self):
        self.salary = int(self.salary * Employee.increment)

    @classmethod
    def change_increment(clss, amount):
        clss.increment = amount

harry = Employee('harry', 'jackson', 44000)
rohan = Employee('rohan', 'das', 44000)

harry.change_increment(3)
harry.increase()
print(harry.salary)