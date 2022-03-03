

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '@' + last + '@company.com'

# if we don't mention self in the method argument and call this method then self will be
# automatically passed and error will be thrown saying fullname() takes 0 positional argument but 1 was given
    def fullname(self):
        return self.first + ' ' + self. last


# instance as first argument and by convention we call instance as self
# instance variables, unique to each instance
emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'User', 60000)


# if we don't have constructor then we can assign each by below way
# emp1.first = 'Corey'
# emp1.last = 'Schafer'
# emp1.email = 'corey.schafer@company.com'
# emp1.pay = 50000
#
# emp2.first = 'Test'
# emp2.last = 'User'
# emp2.email = 'Test.User@company.com'
# emp2.pay = 60000
print(emp1)  # <__main__.Employee object at 0x000002C3C4C386C8>
print(emp1.email)  # Corey@Schafer@company.com
print(emp2.email)  # Test@User@company.com
print(emp1.fullname())
print(emp2.fullname())

# its possible to call method using class name but here instance(emp1) has to be passed manually
print(Employee.fullname(emp1))
