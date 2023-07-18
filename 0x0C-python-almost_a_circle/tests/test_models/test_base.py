#!/usr/bin/python3
'''testcase for base class'''

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''
    Test cases for the Base class.
    '''
    def test_base(self):
        '''testing base'''
        bas1 = Base()
        self.assertEqual(bas1.id, 1)

        bas3 = Base(5)
        self.assertEqual(bas3.id, 5)

        bas2 = Base()
        self.assertEqual(bas2.id, 2)

        if __name__ == '__main__':
            unittest.main()
