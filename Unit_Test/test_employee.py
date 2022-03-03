import unittest
import requests
from unittest.mock import patch
from Unit_Test.employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setup')
        self.emp1 = Employee('Corey', 'Schafer', 50000)
        self.emp2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        print('teardown')

    def test_email(self):
        print('test email')
        self.assertEqual(self.emp1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp2.email, 'Sue.Smith@email.com')

        self.emp1.first = 'John'
        self.emp2.first = 'Jane'

        self.assertEqual(self.emp1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        print('test fullname')
        self.assertEqual(self.emp1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp2.fullname, 'Sue Smith')

        self.emp1.first = 'John'
        self.emp2.first = 'Jane'

        self.assertEqual(self.emp1.fullname, 'John Schafer')
        self.assertEqual(self.emp2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        print('apply raise')
        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 52500)
        self.assertEqual(self.emp2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            return mocked_get


if __name__ == '__main__':
    unittest.main()


'''
setupClass
setup
apply raise
teardown
setup
test email
teardown
setup
test fullname
teardown
tearDownClass


Ran 3 tests in 0.006s

OK

'''