# python Object-Oriented Programming

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

emp_1 = Employee('Richard', 'Wasonga', 50000)
emp_2 = Employee('Test', 'User', 60000)

# print(emp_1)
# print(emp_2)

# print(emp_1.email)
# print(emp_2.email)

# we can run the methods ousing the class name itself but we have to pass in the instance
print(Employee.fullname(emp_1))
print(emp_1.fullname())

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

