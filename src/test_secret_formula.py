import unittest
from secret_formula import subtract_one, plus_ten, add_two_then_square

class SecretFormulaTest(unittest.TestCase):
    def test_subtract_one_10_returns_9(self):
        result = subtract_one(10)
        self.assertEqual(result, 9)
    
    def test_subtract_one_0_returns_minus1(self):
        result = subtract_one(0)
        self.assertEqual(result, -1)
    
    def test_plus_ten_10_returns_20(self):
        result = plus_ten(10)
        self.assertEqual(result, 20)
    
    def test_add_two_then_square_2_return_16(self):
        result = add_two_then_square(2)
        self.assertEqual(result, 16)
