#!/usr/bin/python3
'''testcase for JSON

'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestJson1(unittest.TestCase):
    def test_Save(self):
        '''testing Json'''
        '''save to file'''
        rec = Rectangle(6, 3)
        rec1 = Rectangle(1, 4)
        Rectangle.save_to_file([rec, rec1])
        with open("Rectangle.json", "r") as f:
            d = f.read()
            output = '[{"id": 1, "width": 6, "height": 3, "x": 0, "y": 0}, {"id": 2, "width": 1, "height": 4, "x": 0, "y": 0}]'
            self.assertEqual(d, output)

        rc = Rectangle(6, (3))
        rc1 = Rectangle(1, 4)
        Rectangle.save_to_file([rc, rc1])
        with open("Rectangle.json", "r") as f:
            d = f.read()
            output = '[{"id": 3, "width": 6, "height": 3, "x": 0, "y": 0}, {"id": 4, "width": 1, "height": 4, "x": 0, "y": 0}]'
            self.assertEqual(d, output)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            d2 = f.read()
            output = '[]'
            self.assertEqual(d2, output)

        with self.assertRaises(ValueError):
            rec2 = Rectangle(0, 3)
            rec3 = Rectangle(1, 4)
            Rectangle.save_to_file([rec2, rec3])

        with self.assertRaises(ValueError):
            rec4 = Rectangle(6, 3)
            rec5 = Rectangle(1, -4)
            Rectangle.save_to_file([rec4, rec5])

        with self.assertRaises(ValueError):
            rec6 = Rectangle()
            rec7 = Rectangle()
            Rectangle.save_to_file([rec6, rec7])

        with self.assertRaises(TypeError):
            rc2 = Rectangle((0, 3), 2)
            rc3 = Rectangle(1, 4)
            Rectangle.save_to_file([rc2, rc3])

        with self.assertRaises(TypeError):
            rc4 = Rectangle(4, [3])
            rc5 = Rectangle(1, 4)
            Rectangle.save_to_file([rc4, rc5])

        with self.assertRaises(TypeError):
            rc6 = Rectangle(4, [3, 3])
            rc7 = Rectangle(1, 4)
            Rectangle.save_to_file([rc6, rc7])

        with self.assertRaises(ValueError):
            rc8 = Rectangle(0, 0)
            rc9 = Rectangle(0, 0)
            Rectangle.save_to_file([rc8, rc9])

        sq = Square(4)
        sq = Square(8)
        sq = Square(7)


        if __name__ == '__main__':
            unitest.main()
