# Class Methods As Alternative Constuctor

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

# classmethod start here

    @classmethod
    def from_str(clss, emp_string):
        fname, lname, salary = emp_string.split("-")
        return clss(fname, lname, salary)

harry = Employee('harry', 'jackson', 44000)
rohan = Employee('rohan', 'das', 44000)

lovish = Employee.from_str("lovish-jackson-76000")
print(lovish.fname)