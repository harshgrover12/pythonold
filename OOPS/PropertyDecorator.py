class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@email.com'....commenting it to use it as property

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return '{}.{}@emaill.com'.format(self.first, self.last)

    # we need to have decorator will same name as property name and so the method name
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self, name):
        print('Delete Name!')
        self.first = None
        self.last = None



emp1 = Employee('John', 'Smith')

emp1.first = 'Jim'

emp1.fullname = 'Corey Schafer'  # This property is getting set with setter function

'''
After modifying first name of emp1, first as well as fullname is getting reflected with new name
but email shows old name only as it is not taking value from current object
'''
print(emp1.first)  # Jim
print(emp1.email)  # Jim.Smith@email.com
print(emp1.fullname)  # Jim Smith

del emp1.fullname
