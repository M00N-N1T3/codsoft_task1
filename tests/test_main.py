import unittest
from calculators.advanced.calculator import *


class Addition(unittest.TestCase):

    def test_add_one_value(self):
        result = add([1])
        self.assertEqual(result[0],1)

    def test_add_two_value(self):
        result = add([1,2])
        self.assertEqual(3,result[0])

    def test_add_multiple_value(self):
        result = add([1,2,3,4])
        self.assertEqual(10,result[0])


class Subtraction(unittest.TestCase):
    
    def test_sub_one_value(self):
        result = subs([1])
        self.assertEqual(result[0],1)

    def test_sub_two_value(self):
        result = subs([1,2])
        self.assertEqual(-1,result[0])

    def test_sub_multiple_value_neg(self):
        result = subs([1,2,3,4])
        self.assertEqual(-8,result[0])
    
    def test_sub_multiple_value_pos(self):
        result = subs([10,4,2,1])
        self.assertEqual(3,result[0])


class Multiplication(unittest.TestCase):

    def test_multiplication_one_value(self):
        result = multiplication([1])
        self.assertEqual(1,result[0])

    def test_multiplication_two_value(self):
        result = multiplication([1,2])
        self.assertEqual(2,result[0])

    def test_multiply_multiple_value(self):
        result = multiplication([1,2,3,4])
        self.assertEqual(24,result[0])

    def test_multiply_multiple_by_zero(self):
        result = multiplication([1,2,3,4,0])
        self.assertEqual(0,result[0])

    def test_multiply_multiple_by_neg(self):
        result = multiplication([-1,2,3,4])
        self.assertEqual(-24,result[0])


class Division(unittest.TestCase):

    def test_division_one_value(self):
        result = division([1])
        self.assertEqual(1,result[0])

    def test_division_two_value(self):
        result = division([1,2])
        self.assertEqual(0.5,result[0])

    def test_division_value(self):
        result = division([1,2,3,4])
        self.assertEqual(0.04166666666666666424,result[0])

    def test_division_by_zero(self):
        result = division([1,2,3,4,0])
        self.assertEqual("Error, can not divide by zero!",result[1])

    def test_division_by_neg(self):
        result = division([-1,2,3,4])
        self.assertEqual(-0.041666666666666664,result[0])



if __name__ == "__main__":
    unittest.main()