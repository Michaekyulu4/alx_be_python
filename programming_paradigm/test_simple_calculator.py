import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_addition_positive(self):
        self.assertEqual(self.calc.add(5,7),12)

    def test_addition_negative(self):
        self.assertEqual(self.calc.add(-3, -4), -7)

    def test_addition_mixed(self):
        self.assertEqual(self.calc.add(-8,3),-5)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_subtraction_positive(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtraction_negative_result(self):
        self.assertEqual(self.calc.subtract(3, 5), -2)

    def test_subtraction_zero(self):
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 5), 15)

    def test_multiplication_negative(self):
        self.assertEqual(self.calc.multiply(-2, 4), -8)

    def test_multiplication_by_zero(self):
        self.assertEqual(self.calc.multiply(7, 0), 0)

    # Division Tests
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_negative(self):
        self.assertEqual(self.calc.divide(-9, 3), -3)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(4, 0))

    def test_division_resulting_in_float(self):
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

if __name__ == '__main__':
    unittest.main()

        
