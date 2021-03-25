# Instance and class Variables

class Employee:
    increment = 1.5
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.increment = 1.4
    
    def increase(self):
        self.salary = int(self.salary * Employee.increment)

harry = Employee('harry', 'jackson', 44000)
rohan = Employee('rohan', 'das', 44000)

print(Employee.__dict__)
harry.increase()
print(harry.salary)

# print(harry.fname, rohan.lname)