# Static Methods in Python Oops

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

# staticmethod start here

    @staticmethod
    def isopen(day):
        if day=="Sunday":
            return False
        else:
            return True

harry = Employee('harry', 'jackson', 44000)
rohan = Employee('rohan', 'das', 44000)

# lovish = Employee.from_str("lovish-jackson-76000")
# print(lovish.fname)


print(Employee.isopen("Sunday"))