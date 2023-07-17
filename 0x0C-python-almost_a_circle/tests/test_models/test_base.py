import unittest
from models.base import Base

'''testcase for base class'''


class TestBase(unittest.TestCase):
    '''testing base'''
    def test_Base(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b3 = Base(5)
        self.assertEqual(b3.id, 5)

        b2 = Base()
        self.assertEqual(b2.id, 2)
