import unittest
from Unit_Test import calc


class TestCalc(unittest.TestCase):
    # should have function started with test
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)
        # python -m unittest test_calc to run this file
        # Even if there are 3 asserts, but it is one test only

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertRaises(ValueError, calc.divide, 10, 2)
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()