import unittest
from models.base import Base
from models.rectangle import Rectangle

'''testcase for base and rectangle class'''


class TestBase(unittest.TestCase):
    '''testing base'''
    def test_Base(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b3 = Base(5)
        self.assertEqual(b3.id, 5)

        b2 = Base()
        self.assertEqual(b2.id, 2)

    def tearDown(self):
        '''teardown'''


class TestRectangle(unittest.TestCase):
    '''testing Rectangle'''
    def test_RectangleId(self):
        r1 = Rectangle(3, 6)
        self.assertEqual(r1.id, 3)

        r2 = Rectangle(3, 5, 0, 1)
        self.assertEqual(r2.id, 5)

        r3 = Rectangle(5, 2, 0, 0, 5)
        self.assertEqual(r3.id, 5)

        with self.assertRaises(TypeError):
            r1 = Rectangle()
       
    '''=====================testing for validation======================'''
    def test_RectangleValidation(self):

        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -6)

        with self.assertRaises(ValueError):
            r2 = Rectangle(0, 6)

        with self.assertRaises(TypeError):
            r3 = Rectangle(4, [5])

        with self.assertRaises(Exception):
            r4 = Rectangle(5)

        with self.assertRaises(Exception):
            r5 = Rectangle()

        with self.assertRaises(TypeError):
            r6 = Rectangle(9, 5, [0, 1])

        with self.assertRaises(ValueError):
            r7 = Rectangle(2, 5, 0, -1)

        with self.assertRaises(TypeError):
            r8 = Rectangle(5, 5, 0.2, 1)

        r9 = Rectangle(8, 5, 0, (1))

        with self.assertRaises(TypeError):
            r10 = Rectangle("6", 2, 0, 0, 5)

        with self.assertRaises(TypeError):
            r11 = Rectangle(6, 5, 0, (1, 2))
        
    '''================testing for area=========================='''
    def test_RectangleArea(self):
        r1 = Rectangle(2, 6)
        self.assertEqual(r1.area, 12)

        with self.assertRaises(ValueError):
            r2 = Rectangle(6, -5)

        r3 = Rectangle(2, 2, 0, 0, 5)
        self.assertEqual(r3.area, 12)

        with self.assertRaises(ValueError):
            r4 = Rectangle(0, 6)

        r5 = Rectangle(3, (5), 0, 1)
        self.assertEqual(r5.area, 30)

        with self.assertRaises(TypeError):
            r6 = Rectangle([8], 2, 0, 0, 5)

        with self.assertRaises(ValueError):
            r7 = Rectangle(5, )

        with self.assertRaises(ValueError):
            r8 = Rectangle(4)

        with self.assertRaises(Exception):
            r9 = Rectangle()

        with self.assertRaises(TypeError):
            r10 = Rectangle(3, (5, 1), 0, 1)

        with self.assertRaises(TypeError):
            r11 = Rectangle(7, [5, 1], 0, 1)


if __name__ == '__main__':
    unittest.main
