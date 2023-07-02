#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """test_max will check for various cases
        Checks:
        sorted list, empty list, one value, negative + positive
        unsorted list, negative list, repeated list
    """

    def test_max(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

        result = max_integer([])
        self.assertEqual(result, None)

        result = max_integer([0])
        self.assertEqual(result, 0)

        result = max_integer([-1, -2, 0, -4])
        self.assertEqual(result, 0)

        result = max_integer([1, 6, 9, 4])
        self.assertEqual(result, 9)

        result = max_integer([-3, -2, -7, -4])
        self.assertEqual(result, -2)

        result = max_integer([-1, 7, 0, 4, 7])
        self.assertEqual(result, 7)

        result = max_integer([0, 500])
        self.assertEqual(result, 500)

if __name__ == '__main__':
    unittest.main()
