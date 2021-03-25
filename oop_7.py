# Magic/Dunder Methods In Python

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
            
#-----------------

    def __add__(self, other):
        return self.salary + other.salary

    def __repr__(self):
        return 'Employee({}, {}, {})'.format(self.fname, self.lname, self.salary)

    def __str__(self):
        return 'The name of employee is {}'.format(self.fname)

harry = Employee('harry', 'jackson', 44000)
rohan = Employee('rohan', 'agarwal', 9)

a = 6
print(a.__mul__(7))

# search on google [ build in dunder methods in python ]

print(repr(harry))
# print(str(harry))