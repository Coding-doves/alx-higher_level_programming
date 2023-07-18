#!/usr/bin/python3

'''
Testcase for rectangle class
    1. initialization test  -> 18
    2. setters test         -> 26
    3. validation test      -> 38
    4. area test            -> 80
    5. display test         -> 143
    6. str test             -> 232
    7. update test          -> 271

'''
import unittest
import io
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    '''
    Testing Rectangle
    '''
    def test_rectangle_initialized(self):
        '''testing Rectangle'''
        rec = Rectangle(10, 20, 2, 3, 6)
        self.assertEqual(rec.id, 6)
        self.assertEqual(rec.width, 10)
        self.assertEqual(rec.height, 20)
        self.assertEqual(rec.x, 2)
        self.assertEqual(rec.y, 3)

    def test_rectangle_setter(self):
        '''testing Rectangle'''
        sett = Rectangle(10, 20, 2, 3)
        sett.width = 11
        sett.height = 15
        sett.x = 4
        sett.y = 1
        self.assertEqual(sett.width, 11)
        self.assertEqual(sett.height, 15)
        self.assertEqual(sett.x, 4)
        self.assertEqual(sett.y, 1)


    def test_rectangle_validation(self):
        '''testing for validation'''

        with self.assertRaises(ValueError):
            Rectangle(1, -6)
            Rectangle(0, 0)
            Rectangle(0, 6)
            Rectangle(2, 5, 0, -1)
            Rectangle(5, )

        with self.assertRaises(Exception):
            Rectangle(5)
            Rectangle()

        with self.assertRaises(TypeError):
            Rectangle(9, 5, [0, 1])
            Rectangle(5, 5, 0.2, 1)
            Rectangle("6", 2, 0, 0, 5)
            Rectangle(6, 5, 0, (1, 2))
            Rectangle(4, [5])

    def test_rectangle_area(self):
        '''testing for area'''
        a_s1 = Rectangle(2, 6)
        self.assertEqual(a_s1.area(), 12)

        a_s2 = Rectangle(2, 2, 0, 0, 5)
        self.assertEqual(a_s2.area(), 4)

        a_s3 = Rectangle(3, (5), 0, 1)
        self.assertEqual(a_s3.area(), 15)

        with self.assertRaises(ValueError):
            a_s4 = Rectangle(0, 0)
            a_s4.area()

            a_s4 = Rectangle(1, -6)
            a_s4.area()

            a_s5 = Rectangle(0, 6)
            a_s5.area()

            a_s10 = Rectangle(2, 5, 0, -1)
            a_s10.area()

            a_s = Rectangle(5, )
            a_s.area()

        with self.assertRaises(Exception):
            a_s7 = Rectangle(5)
            a_s7.area()

            a_s8 = Rectangle()
            a_s8.area()

            a_s14 = Rectangle()
            a_s14.area()


        with self.assertRaises(TypeError):
            a_s9 = Rectangle(9, 5, [0, 1])
            a_s9.area()

            a_s6 = Rectangle(4, [5])
            a_s6.area()

            a_s11 = Rectangle(5, 5, 0.2, 1)
            a_s11.area()

            a_s12 = Rectangle("6", 2, 0, 0, 5)
            a_s12.area()

            a_s13 = Rectangle(6, 5, 0, (1, 2))
            a_s13.area()

    def test_rectangle_display(self):
        '''testing for display `#` a output'''
        d_s = Rectangle(2, 3)
        output = '##\n##\n##\n'
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            d_s.display()
            self.assertEqual(fake_stdout.getvalue(), output)

        d_s1 = Rectangle((2), 3)
        outp = '##\n##\n##\n'
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            d_s1.display()
            self.assertEqual(fake_stdout.getvalue(), outp)

        d_s10 = Rectangle(2, 3, 0, (1))
        outp1 = '\n##\n##\n##\n'
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            d_s10.display()
            self.assertEqual(fake_stdout.getvalue(), outp1)

        d_s12 = Rectangle((2), 3, 0, 0)
        outp2 = '##\n##\n##\n'
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            d_s12.display()
            self.assertEqual(fake_stdout.getvalue(), outp2)

        with self.assertRaises(ValueError):
            d_s2 = Rectangle(2, 0)
            d_s2.display()

            d_s3 = Rectangle(0, 0)
            d_s3.display()

            d_s4 = Rectangle(-2, 2)
            d_s4.display()

            d_s11 = Rectangle(2, 1, -1, 1)
            d_s11.display()

        with self.assertRaises(TypeError):
            d_s5 = Rectangle(3, [5], 0, 1)
            d_s5.display()

            d_s6 = Rectangle((2, 4), 2)
            d_s6.display()

            d_s7 = Rectangle(2, [7, 2])
            d_s7.display()

            d_s8 = Rectangle('2', 2)
            d_s8.display()

            d_s9 = Rectangle(2, 2.9)
            d_s9.display()

            d_s14 = Rectangle(3, 5, [0], 1)
            d_s14.display()

            d_s15 = Rectangle(2, 4, (1, 0), 2)
            d_s15.display()

            d_s16 = Rectangle(2, 6, [7, 2], 4)
            d_s16.display()

            d_s17 = Rectangle(4, 1, '2', 2)
            d_s17.display()

            d_s18 = Rectangle(4, 1, 2, 2.9)
            d_s18.display()

    def test_str(self):
        '''testing str'''
        re_s = Rectangle(10, 30, 2, 3)
        ex_out = f"[Rectangle] ({re_s.id}) 2/3 - 10/30"
        self.assertEqual(str(re_s), ex_out)

        re1 = Rectangle(10, 30)
        ex_out = f"[Rectangle] ({re1.id}) 0/0 - 10/30"
        self.assertEqual(str(re1), ex_out)

        with self.assertRaises(TypeError):
            re2 = Rectangle(4, 1, '2', 2)
            re2.__str__()

            re3 = Rectangle(4, 1, 2, 2.9)
            re3.__str__()

            re6 = Rectangle(3, 5, [0], 1)
            re6.__str__()

            re7 = Rectangle(2, 4, (1, 0), 2)
            re7.__str__()

            re8 = Rectangle(2, 6, [7, 2], 4)
            re8.__str__()

        with self.assertRaises(ValueError):
            re4 = Rectangle(2, 1, -1, 1)
            re4.__str__()

    def test_update(self):
        '''testing update'''
        up_u = Rectangle(10, 30, 17, 2, 3)
        up_k = Rectangle(10, 30, 17, 2, 3)

        up_u.update(100, 5, 6, 0)
        self.assertEqual(up_u.width, 5)
        self.assertEqual(up_u.x, 0)
        self.assertEqual(up_u.y, 2)
        self.assertEqual(up_u.height, 6)
        self.assertEqual(up_u.id, 100)

        up_k.update(id=70, width=15, height=16)
        self.assertEqual(up_k.width, 15)
        self.assertEqual(up_k.x, 17)
        self.assertEqual(up_k.y, 2)
        self.assertEqual(up_k.height, 16)
        self.assertEqual(up_k.id, 70)

        up_2 = Rectangle(10, 30)
        up_2.update(100, 5, 6, (0), 0)
        self.assertEqual(up_2.width, 5)
        self.assertEqual(up_2.x, 0)
        self.assertEqual(up_2.y, 0)
        self.assertEqual(up_2.height, 6)
        self.assertEqual(up_2.id, 100)

        up_k2 = Rectangle(10, 30)
        up_k2.update(id=10, width=8, height=14, x=(2), y=3)
        self.assertEqual(up_k2.width, 8)
        self.assertEqual(up_k2.x, 2)
        self.assertEqual(up_k2.y, 3)
        self.assertEqual(up_k2.height, 14)
        self.assertEqual(up_k2.id, 10)

        with self.assertRaises(TypeError):
            up_u.update(100, [5], 6, 0)
            up_u.update(100, 5, '6', 0)
            up_u.update(100, (5, 6))
            up_u.update(100, [5, 0], 6, 0)
            up_k.update(id=100, width=[5], height=6)
            up_k.update(id=100, width='5', height=6)
            up_k.update(id=100, width=(5, 6), height=6)
            up_k.update(id=100, width=[5, 0], height=6, x= 0)

        with self.assertRaises(ValueError):
            up_k.update(id=100, width=5, height=-6)
            up_u.update(100, -5, 6, 0)



if __name__ == '__main__':
    unittest.main()
