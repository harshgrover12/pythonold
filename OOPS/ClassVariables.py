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

# self.raise_amt, in above method will give flexibility to change it for instances


emp1 = Employee('Corey', 'Schafer', 5000)
emp2 = Employee('Test', 'User', 5000)

# class variables can be accessed via class as well instance.
print(Employee.raise_amt)  # 1.04
print(emp1.raise_amt)  # 1.04
print(emp1.pay)

#
print(Employee.__dict__)
'''
raise_amt is part of dict

{'__module__': '__main__', 'raise_amt': 1.04, '__init__': <function Employee.__init__ at 0x000001EAECED5B88>,
 'fullname': <function Employee.fullname at 0x000001EAECED5C18>,
  'apply_raise': <function Employee.apply_raise at 0x000001EAECED5CA8>,
   '__dict__': <attribute '__dict__' of 'Employee' objects>, 
   '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}

'''
print(emp1.__dict__)  #  {'first': 'Corey', 'last': 'Schafer', 'pay': 5000}, no raise_amt variable

# Employee.raise_amt = 1.05

print(Employee.raise_amt)
emp1.raise_amt = 1.05
print(emp1.raise_amt) # 1.05
print(emp1.__dict__)  # {'first': 'Corey', 'last': 'Schafer', 'pay': 5000, 'raise_amt': 1.05},
# now raise_amt is there in namespace
print(emp2.raise_amt)  # 1.04
print(Employee.num_of_emps)  # 2, as 2 employees are instantiated
