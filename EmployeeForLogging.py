import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        logger.info('Created Employee: {} {}'.format(self.fullname, self.email))
        '''
        INFO:__main__:Created Employee: John Smith John.Smith@email.com
        INFO:__main__:Created Employee: Corey Schafer Corey.Schafer@email.com
I       NFO:__main__:Created Employee: Jane Doe Jane.Doe@email.com
        '''


    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('John', 'Smith')
emp2 = Employee('Corey', 'Schafer')
emp3 = Employee('Jane', 'Doe')