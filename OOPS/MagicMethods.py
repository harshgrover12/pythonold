# Dunder methods

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return self.fullname()


emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'Employee', 60000)
print(emp1)  # <__main__.Employee object at 0x0000020C1A991648>
print(emp1.__repr__())  # Employee('Corey', 'Schafer', 50000), after implementing repr method
print(emp1)  # after implementing str dunder method, by default it will call that method
# on print emp1 object for which output is Corey Schafer - Corey.Schafer@email.com

print(1+2) , # this in background calls __add__ dunder method of int class
print(int.__add__(1, 2))
print(str.__add__('a', 'b'))  # ab
print(emp1 + emp2)  # 110000, after implementing add dunder method in the class
print('test'.__len__())  # 4
print(len(emp1))

