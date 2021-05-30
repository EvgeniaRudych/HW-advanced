import unittest
from unittest.mock import patch
from calc import Calculator


class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(4, 5), 9)
        self.assertEqual(Calculator.add(1, 2), 3)
        self.assertRaises(TypeError, Calculator.add, "x", 2)
        self.assertRaises(TypeError, Calculator, [], 3)

    def test_substract(self):
        self.assertEqual(Calculator.subtract(6, 3), 3)
        self.assertEqual(Calculator.subtract(4, 4), 0)
        self.assertRaises(TypeError, Calculator.subtract, "mario", 3)
        self.assertRaises(TypeError, Calculator.subtract, {1,2}, 4)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(0, 3), 0)
        self.assertEqual(Calculator.multiply(1,2), 2)
        self.assertEqual(Calculator.multiply("3", 3),"333")
        self.assertEqual(Calculator.multiply("e", 5), "eeeee")
        self.assertRaises(TypeError, Calculator.multiply, None, 2)

    def test_divide(self):
        self.assertEqual(Calculator.divide(3, 3), 1)
        self.assertEqual(Calculator.divide(-9,3), -3)
        self.assertRaises(TypeError, Calculator.divide, None, 3)
        self.assertRaises(TypeError, Calculator.divide, "q", 2)
        self.assertRaises(ValueError, Calculator.divide, 10, 0)


if __name__ == "__main__":
    unittest.main()
