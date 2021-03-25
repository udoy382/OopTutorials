# Inheritance In Python oops

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
    
    @classmethod
    def from_str(clss, emp_string):
        fname, lname, salary = emp_string.split("-")
        return clss(fname, lname, salary)

    def isopen(day):
        if day=="Sunday":
            return False
        else:
            return True
# start here

class Programmer(Employee):
    def __init__(self, fname, lname, salary, proglang):
        super().__init__(fname, lname, salary)
        self.proglang = proglang

    def increase(self):
        self.salary = int(self.salary * (Employee.increment+0.2))


udoy = Programmer('udoy', 'rahman', 5566, 'python')
help(Employee)

#-----------------
# harry = Employee('harry', 'jackson', 44000)
# rohan = Employee('rohan', 'das', 44000)

# print(Employee.isopen("Sunday"))