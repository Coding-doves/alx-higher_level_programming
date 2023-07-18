#!/usr/bin/python3

'''testcase for square class
    1. initialization test  -> 18
    2. setters test         -> 25
    3. validation test      -> 35
    4. area test            -> 69
    5. display test         -> 121
    6. str test             -> 206
    7. update test          -> 245

'''
import io
from unittest.mock import patch
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    '''
    testing Square
    prototype
    '''
    def test_square_initialized(self):
        '''testing initialization'''
        squ = Square(10, 2, 3, 6)
        self.assertEqual(squ.id, 6)
        self.assertEqual(squ.size, 10)
        self.assertEqual(squ.x, 2)
        self.assertEqual(squ.y, 3)

    def test_square_setter(self):
        '''testing setter'''
        seet = Square(10, 2, 2, 3)
        seet.size = 11
        seet.x = 4
        seet.y = 1
        self.assertEqual(seet.size, 11)
        self.assertEqual(seet.x, 4)
        self.assertEqual(seet.y, 1)


    def test_square_validation(self):
        '''testing for validation'''

        with self.assertRaises(ValueError):
            Square(-6)
            Square(0)
            Square(5, 0, -1)

        with self.assertRaises(TypeError):
            Square([5])
            Square(9, 5, [0, 1])
            Square(0.2, 1)
            Square("6", 0, 0, 5)
            Square(5, 0, (1, 2))

        with self.assertRaises(Exception):
            Square()

    def test_square_area(self):
        '''testing for area'''
        sq_a1 = Square(6)
        self.assertEqual(sq_a1.area(), 36)

        sq_a2 = Square(2, 0, 0, 5)
        self.assertEqual(sq_a2.area(), 4)

        sq_a3 = Square((5), 0, 1)
        self.assertEqual(sq_a3.area(), 25)

        with self.assertRaises(ValueError):
            sq_a4 = Square(-6)
            sq_a4.area()

            sq_a5 = Square(0)
            sq_a5.area()

            sq_a10 = Square(2, 0, -1)
            sq_a10.area()

        with self.assertRaises(Exception):
            sq_a8 = Square()
            sq_a8.area()

            sq_a14 = Square()
            sq_a14.area()

        with self.assertRaises(TypeError):
            sq_a9 = Square(9, 5, [0, 1])
            sq_a9.area()

            sq_a6 = Square([5])
            sq_a6.area()

            sq_a11 = Square(5, 0.2, 1)
            sq_a11.area()

            sq_a12 = Square("6", 0, 0, 5)
            sq_a12.area()

            sq_a13 = Square(6, 0, (1, 2))
            sq_a13.area()

    def test_square_display(self):
        '''testing for display `#` a output'''
        sq_d = Square(2, 3)
        output = '   ##\n   ##\n'
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            sq_d.display()
            self.assertEqual(fake_stdout.getvalue(), output)

        sq_d1 = Square((2), 3)
        outp = '   ##\n   ##\n'
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            sq_d1.display()
            self.assertEqual(fake_stdout.getvalue(), outp)

        dd1 = Square(3, 0, (1))
        outp1 = '\n###\n###\n###\n'
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            dd1.display()
            self.assertEqual(fake_stdout.getvalue(), outp1)

        dd2 = Square((2), 0, 0)
        outp2 = '##\n##\n'
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            dd2.display()
            self.assertEqual(fake_stdout.getvalue(), outp2)

        with self.assertRaises(ValueError):
            sq_d2 = Square(0)
            sq_d2.display()

            sq_d4 = Square(-2)
            sq_d4.display()

            dd2 = Square(2, -1, 1)
            dd2.display()

        with self.assertRaises(TypeError):
            sq_d5 = Square([5], 0, 1)
            sq_d5.display()

            sq_d6 = Square((2, 4))
            sq_d6.display()

            sq_d7 = Square([7, 2])
            sq_d7.display()

            sq_d8 = Square('2')
            sq_d8.display()

            sq_d9 = Square(2.9)
            sq_d9.display()

            dd3 = Square(3, 1, '0')
            dd3.display()

            dd5 = Square(5, [0], 1)
            dd5.display()

            dd6 = Square(4, (1, 0), 2)
            dd6.display()

            dd7 = Square(6, [7, 2], 4)
            dd7.display()

            dd8 = Square(1, '2', 2)
            dd8.display()

            dd9 = Square(4, 2, 2.9)
            dd9.display()

    def test_str(self):
        '''testing str'''
        sq_re = Square(10, 30, 2, 3)
        ex_out = f"[Square] ({sq_re.id}) 30/2 - 10"
        self.assertEqual(str(sq_re), ex_out)

        re1 = Square(10, 30, 3)
        ex_out = f"[Square] ({re1.id}) 30/3 - 10"
        self.assertEqual(str(re1), ex_out)

        with self.assertRaises(TypeError):
            re2 = Square(4, '2', 2)
            re2.__str__()

            re3 = Square(1, 2, 2.9)
            re3.__str__()

            re5 = Square(9, 1, '0')
            re5.__str__()

            re6 = Square(5, [0], 1)
            re6._str()

            re7 = Square(4, (1, 0), 2)
            re7.__str__()

            re8 = Square(6, [7, 2], 4)
            re8.__str__()

        with self.assertRaises(ValueError):
            re4 = Square(2, -1, 1)
            re4.__str__()

    def test_update(self):
        '''testing update'''
        up_s = Square(10, 7, 2, 3)
        up_k = Square(10, 7, 2, 3)

        up_s.update(100, 5, 6, 0)
        self.assertEqual(up_s.size, 5)
        self.assertEqual(up_s.x, 6)
        self.assertEqual(up_s.y, 0)
        self.assertEqual(up_s.id, 100)

        up_k.update(id=70, size=15)
        self.assertEqual(up_k.x, 7)
        self.assertEqual(up_k.y, 2)
        self.assertEqual(up_k.size, 15)
        self.assertEqual(up_k.id, 70)

        up_s2 = Square(10)
        up_s2.update(100, 6, (0), 0)
        self.assertEqual(up_s2.x, 0)
        self.assertEqual(up_s2.y, 0)
        self.assertEqual(up_s2.size, 6)
        self.assertEqual(up_s2.id, 100)

        up_k2 = Square(10)
        up_k2.update(id=10, size=8, x=(2), y=3)
        self.assertEqual(up_k2.size, 8)
        self.assertEqual(up_k2.x, 2)
        self.assertEqual(up_k2.y, 3)
        self.assertEqual(up_k2.id, 10)

        with self.assertRaises(ValueError):
            up_s.update(100, -5, 6, 0)
            up_k.update(id=100, size=-6)

        with self.assertRaises(TypeError):
            up_s.update(100, 5, '6', 0)
            up_s.update(100, (5, 6))
            up_s.update(100, [5, 0], 6, 0)
            up_k.update(id=100, size=[5])
            up_s.update(100, [5], 6, 0)
            up_k.update(id=100, size='5')
            up_k.update(id=100, size=(5, 6))
            up_k.update(id=100, size=[5, 0], x= 0)

    def test_create_square(self):
        '''testing create'''
        creat_s = {'size': 10, 'x': 1, 'y': 2, 'id': 43}
        ct_s = Square.create(**creat_s)

        self.assertEqual(ct_s.size, 10)
        self.assertEqual(ct_s.x, 1)
        self.assertEqual(ct_s.y, 2)
        self.assertEqual(ct_s.id, 43)

        creat_s2 = {'size': (10), 'x': 1, 'y': 2, 'id': 43}
        ct_s2 = Square.create(**creat_s2)

        self.assertEqual(ct_s2.size, 10)
        self.assertEqual(ct_s2.x, 1)
        self.assertEqual(ct_s2.y, 2)
        self.assertEqual(ct_s2.id, 43)

        with self.assertRaises(TypeError):
            ct_s0 = {'id': 100, 'width': [5], 'height': 6}
            Square.create(**ct_s0)
        with self.assertRaises(TypeError):
            ct_s1 = {'id': 100, 'width': '5', 'height': 6}
            Square.create(**ct_s1)
        with self.assertRaises(TypeError):
            ct_s2 = {'id': 100, 'width': (5, 6), 'height': 6}
            Square.create(**ct_s2)
        with self.assertRaises(TypeError):
            ct_s3 = {'id': 100, 'width': [5, 0], 'height': 6, 'x': 0}
            Square.create(**ct_s3)

        with self.assertRaises(ValueError):
            ct_s = {'id': 100, 'width': 5, 'height': -6}
            Square.create(**ct_s)


if __name__ == '__main__':
    unittest.main()
