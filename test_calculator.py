import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add2(self):
        self.assertEqual(self.calc.add(4, 2), 6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(9, 2), 7)

    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(10, 2), 8)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(10, 10), 100) 

    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(4, 2), 8)   

    def test_divide(self):
        self.assertEqual(self.calc.divide(50, 2), 25)

    def test_divide2(self):
        self.assertEqual(self.calc.divide(8, 2), 4) 

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1) 

    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(34, 7), 6)


if __name__ == '__main__':
    unittest.main()