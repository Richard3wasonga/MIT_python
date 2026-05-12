# python Object-Oriented Programming

class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str_1.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Richard', 'Wasonga', 50000)
emp_2 = Employee('Test', 'User', 60000)

import datetime
my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))

# Employee.set_raise_amt(1.05)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# In this use case where someone needs to parse manually a string before making a new employee 

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'

# first, last, pay = emp_str_1.split('-')

# new_emp_1 = Employee(first, last, pay)

# The class method found_string return the employee object created thus using the class method as an alternative constructor

# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)



# Here in number of employees there is no need to use self because we don't have a use case where a instance would need it and 
# put it under init because every time an object is created the __init__ runs

# print(Employee.num_of_emps)

# when we change using the class it updates for all but if we change using emp_1 it makes a raise amount instance variable for 
# only emp_1 and the other instances fall back to the class raise amount hence in the apply raise method you get why it is 
# benefitial to use self and not employee since you can modify the raise amount for a specific employee

# print(emp_1.__dict__)

# Employee.raise_amount = 1.05
# emp_1.raise_amount = 1.05

# print(emp_1.__dict__)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(emp_1.email)
# print(emp_2.email)

# we can run the methods ousing the class name itself but we have to pass in the instance
# print(Employee.fullname(emp_1))
# print(emp_1.fullname())

# We would do this physically as so without assistance of classes 

# emp_1.first = 'Richard'
# emp_1.last = 'Wasonga'
# emp_1.email = 'richard.wasonga@company.com'
# emp_1.pay = 50000

# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'test.user@company.com'
# emp_2.pay = 60000

# print('{} {}'.format(emp_1.first, emp_1.last))

