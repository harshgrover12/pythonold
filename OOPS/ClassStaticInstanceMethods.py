class Employee:

    raise_amt = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amt)

    @classmethod
    def set_raise(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee('Corey', 'Schafer', 5000)
emp2 = Employee('Test', 'User', 5000)

# class variables can be accessed via class as well instance.
print(Employee.raise_amt)  # 1.04
print(emp1.raise_amt)  # 1.04
print(emp2.raise_amt)  # 1.04
print(emp1.set_raise(1.05))

emp_str_1 = 'John-Doe-70000'
new_emp_1 = Employee.from_string(emp_str_1)

import datetime
my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))  # False, static method has no relation to instance or class variables.


