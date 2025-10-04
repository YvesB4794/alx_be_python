import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Create a new SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # ------------------------
    # Addition Tests
    # ------------------------
    def test_addition(self):
        """Test addition of positive, negative, and zero values."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertEqual(self.calc.add(0, 10), 10)

    # ------------------------
    # Subtraction Tests
    # ------------------------
    def test_subtraction(self):
        """Test subtraction with various inputs."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertEqual(self.calc.subtract(0, 7), -7)

    # ------------------------
    # Multiplication Tests
    # ------------------------
    def test_multiplication(self):
        """Test multiplication of integers and zero."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(-2, -8), 16)

    # ------------------------
    # Division Tests
    # ------------------------
    def test_division(self):
        """Test normal division and division by zero."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertEqual(self.calc.divide(0, 5), 0)

        # Division by zero should return None
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    # ------------------------
    # Edge Case Tests
    # ------------------------
    def test_division_with_floats(self):
        """Test division with floating-point numbers."""
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertAlmostEqual(self.calc.divide(-9.0, 3.0), -3.0)

    def test_large_numbers(self):
        """Test operations with very large numbers."""
        large_num = 10**10
        self.assertEqual(self.calc.add(large_num, 1), large_num + 1)
        self.assertEqual(self.calc.multiply(large_num, 2), large_num * 2)


if __name__ == "__main__":
    unittest.main()

