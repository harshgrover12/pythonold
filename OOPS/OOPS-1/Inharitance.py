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

# passing Employee as argument to Developer gives access to all the attributes of Employee class
class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp  in self.employees:
            self.employees.remove(emp)

    def print_employee(self):
        for emp in self.employees:
            print('--->', emp.fullname())



dev1 = Developer('Harsh', 'Grover', 10000, 'python')
dev2 = Developer('Tarun','Yadav', 60000, 'Java')
print(dev1.pay)
print(dev1.fullname())

mgr1 = Manager('Sue', 'Smith', 90000, [dev1])
print(mgr1.email)  # Sue.Smith@email.com
mgr1.add_employee(dev2)
mgr1.remove_employee(dev1)
mgr1.print_employee()  # ---> Tarun Yadav

# dev1.apply_raise()
# print(dev1.pay)  # 10400, when Developer class doesn't modify the variable and uses inherited class var
dev1.apply_raise()
print(dev1.pay)  # 11000 when variable is modified at Developer class
print(dev1.email)  # Harsh.Grover@email.com
print(dev1.prog_lang)  # python
print(dev2.pay)  # 60000


# isinstance and issubclass
print(isinstance(mgr1, Manager))  # True
print(isinstance(mgr1, Employee))  # True
print(isinstance(mgr1, Developer))  # False

print(issubclass(Developer, Employee))  # True
print(issubclass(Manager, Employee))  # True
print(issubclass(Manager, Developer))  # False

# Real word example
# HTTPException is subsclass of Exception and HTTPException is super class for all the HTTP exception code
