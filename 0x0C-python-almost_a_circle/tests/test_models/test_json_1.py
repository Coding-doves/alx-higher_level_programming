#!/usr/bin/python3
'''
Testcase for JSON

'''
import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestJson1(unittest.TestCase):
    '''
    Testcase for JSON
    '''
    def test_save(self):
        '''save to file'''
        rec = Rectangle(6, 3)
        rec1 = Rectangle(1, 4)
        Rectangle.save_to_file([rec, rec1])
        with open("Rectangle.json", "r", encoding='utf=8') as fil:
            d_fy = fil.read()
            output = (f'[{{"id": {rec.id}, "width": 6, "height": 3, "x": 0, "y": 0}}, '
                  f'{{"id": {rec1.id}, "width": 1, "height": 4, "x": 0, "y": 0}}]')
            self.assertEqual(d_fy, output)

        s_rc = Rectangle(6, (3))
        rc1 = Rectangle(1, 4)
        Rectangle.save_to_file([s_rc, rc1])
        with open("Rectangle.json", "r", encoding='utf=8') as fil:
            d_fy = fil.read()
            output = (f'[{{"id": {s_rc.id}, "width": 6, "height": 3, "x": 0, "y": 0}}, '
                     f'{{"id": {rc1.id}, "width": 1, "height": 4, "x": 0, "y": 0}}]')
            self.assertEqual(d_fy, output)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r", encoding='utf=8') as fil:
            d_fy2 = fil.read()
            output = '[]'
            self.assertEqual(d_fy2, output)

        with self.assertRaises(ValueError):
            rec2 = Rectangle(0, 3)
            rec3 = Rectangle(1, 4)
            Rectangle.save_to_file([rec2, rec3])

            rc8 = Rectangle(0, 0)
            rc9 = Rectangle(0, 0)
            Rectangle.save_to_file([rc8, rc9])

            rec4 = Rectangle(6, 3)
            rec5 = Rectangle(1, -4)
            Rectangle.save_to_file([rec4, rec5])

            rec6 = Rectangle()
            rec7 = Rectangle()
            Rectangle.save_to_file([rec6, rec7])

        with self.assertRaises(TypeError):
            rc2 = Rectangle((0, 3), 2)
            rc3 = Rectangle(1, 4)
            Rectangle.save_to_file([rc2, rc3])

            rc4 = Rectangle(4, [3])
            rc5 = Rectangle(1, 4)
            Rectangle.save_to_file([rc4, rc5])

            rc6 = Rectangle(4, [3, 3])
            rc7 = Rectangle(1, 4)
            Rectangle.save_to_file([rc6, rc7])

    def test_save_square(self):
        ''' save to file '''
        squ = Square(4)
        squ1 = Square(8)
        Square.save_to_file([squ, squ1])
        with open("Square.json", "r", encoding='utf=8') as fil:
            d_fy = fil.read()
            output = (f'[{{"id": {squ.id}, "size": 4, "x": 0, "y": 0}}, '
                      f'{{"id": {squ1.id}, "size": 8, "x": 0, "y": 0}}]')
            self.assertEqual(d_fy, output)

        squ0 = Square(7)
        squ2 = Square((4))
        Square.save_to_file([squ0, squ2])
        with open("Square.json", "r", encoding='utf=8') as fil:
            d_fy = fil.read()
            output = (f'[{{"id": {squ0.id}, "size": 7, "x": 0, "y": 0}}, '
                      f'{{"id": {squ2.id}, "size": 4, "x": 0, "y": 0}}]')
            self.assertEqual(d_fy, output)

        Square.save_to_file(None)
        with open("Square.json", "r", encoding='utf=8') as fil:
            d_fy2 = fil.read()
            output = '[]'
            self.assertEqual(d_fy2, output)

        with self.assertRaises(ValueError):
            squr2 = Square(0)
            squr3 = Square(1)
            Square.save_to_file([squr2, squr3])

            squr = Square(0)
            squr = Square(0)
            Square.save_to_file([squr, squr])

            squr4 = Square(6)
            squr5 = Square(-4)
            Square.save_to_file([squr4, squr5])

            squr6 = Square()
            squr7 = Square()
            Square.save_to_file([squr6, squr7])

        with self.assertRaises(TypeError):
            squr2 = Square((0, 3))
            squr3 = Square(1)
            Square.save_to_file([squr2, squr3])

            squr4 = Square([3])
            squr5 = Square(4)
            Square.save_to_file([squr4, squr5])

            squr6 = Square([3, 3])
            squr7 = Square(4)
            Square.save_to_file([squr6, squr7])



        if __name__ == '__main__':
            unittest.main()
