import unittest

# This is the class we want to test
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b

# This is the test class for our Calculator
class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Set up for test methods."""
        self.calculator = Calculator()

    def test_add(self):
        """Test the add method."""
        self.assertEqual(self.calculator.add(5, 3), 8)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(-1, -1), -2)

    def test_subtract(self):
        """Test the subtract method."""
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(3, 5), -2)
        self.assertEqual(self.calculator.subtract(10, 0), 10)

    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calculator.multiply(5, 3), 15)
        self.assertEqual(self.calculator.multiply(5, 0), 0)
        self.assertEqual(self.calculator.multiply(-2, 4), -8)

    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calculator.divide(10, 2), 5)
        self.assertAlmostEqual(self.calculator.divide(7, 3), 2.3333333333333335) # For floating point precision
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)

if __name__ == '__main__':
    unittest.main()