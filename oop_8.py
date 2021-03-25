# Property Decorators, Setters & Deleters


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

    @email.setters
    def email(self, given_email):
        name_list = given_email.split('@')[0].split('.')
        print(given_email)
        self.fname = name_list[0]
        self.lname = name_list[1]

    @property
    def email(self):
        return self.fname +'.'+ self.lname + '@gmail.com'

    @email.deleter
        if self.fname == None:
            return 'email not set'
        else:
            return 'email is set'

    def email(self):
        self.fname = None
        self.lname = None

if __name__ == '__main__':
    harry = Employee('harry', 'jackson', 44000)
    rohan = Employee('rohan', 'agarwal', 9)
    print(harry.email)
    print(rohan.email)
    rohan.lname = 'Khanna'
    print(rohan.email)
    rohan.email = 'kannarohan@gmail.com'
    print(rohan.email)