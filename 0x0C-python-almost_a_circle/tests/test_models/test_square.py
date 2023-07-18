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
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    '''testing Square'''
    def test_SquareInitialized(self):
        sq = Square(10, 2, 3, 6)
        self.assertEqual(sq.id, 6)
        self.assertEqual(sq.size, 10)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 3)
       
    def test_SquareSetter(self):
        Set = Square(10, 2, 2, 3)
        Set.size = 11
        Set.x = 4
        Set.y = 1
        self.assertEqual(Set.size, 11)
        self.assertEqual(Set.x, 4)
        self.assertEqual(Set.y, 1)


    '''=====================testing for validation======================'''
    def test_SquareValidation(self):

        with self.assertRaises(ValueError):
            r1 = Square(-6)

        with self.assertRaises(ValueError):
            r2 = Square(0)

        with self.assertRaises(TypeError):
            r3 = Square([5])

        with self.assertRaises(Exception):
            r5 = Square()

        with self.assertRaises(TypeError):
            r6 = Square(9, 5, [0, 1])

        with self.assertRaises(ValueError):
            r7 = Square(5, 0, -1)

        with self.assertRaises(TypeError):
            r8 = Square(0.2, 1)

        with self.assertRaises(TypeError):
            r10 = Square("6", 0, 0, 5)

        with self.assertRaises(TypeError):
            r11 = Square(5, 0, (1, 2))
        
        with self.assertRaises(Exception):
            r12 = Square()


    '''================testing for area=========================='''
    def test_SquareArea(self):
        a1 = Square(6)
        self.assertEqual(a1.area(), 36)

        a2 = Square(2, 0, 0, 5)
        self.assertEqual(a2.area(), 4)

        a3 = Square((5), 0, 1)
        self.assertEqual(a3.area(), 25)

        with self.assertRaises(ValueError):
            a4 = Square(-6)
            a4.area()

        with self.assertRaises(ValueError):
            a5 = Square(0)
            a5.area()

        with self.assertRaises(TypeError):
            a6 = Square([5])
            a6.area()

        with self.assertRaises(Exception):
            a8 = Square()
            a8.area()

        with self.assertRaises(TypeError):
            a9 = Square(9, 5, [0, 1])
            a9.area()

        with self.assertRaises(ValueError):
            a10 = Square(2, 0, -1)
            a10.area()

        with self.assertRaises(TypeError):
            a11 = Square(5, 0.2, 1)
            a11.area()

        with self.assertRaises(TypeError):
            a12 = Square("6", 0, 0, 5)
            a12.area()

        with self.assertRaises(TypeError):
            a13 = Square(6, 0, (1, 2))
            a13.area()
        
        with self.assertRaises(Exception):
            a14 = Square()
            a14.area()


    '''=============testing for display `#` a output========================'''
    def test_SquareDisplay(self):
        import io
        from unittest.mock import patch
        d = Square(2, 3)
        output = '   ##\n   ##\n'
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            d.display()
            self.assertEqual(fake_stdout.getvalue(), output)

        d1 = Square((2), 3)
        outp = '   ##\n   ##\n'
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            d1.display()
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
            d2 = Square(0)
            d2.display()

        with self.assertRaises(ValueError):
            d4 = Square(-2)
            d4.display()

        with self.assertRaises(TypeError):
            d5 = Square([5], 0, 1)
            d5.display()

        with self.assertRaises(TypeError):
            d6 = Square((2, 4))
            d6.display()

        with self.assertRaises(TypeError):
            d7 = Square([7, 2])
            d7.display()

        with self.assertRaises(TypeError):
            d8 = Square('2')
            d8.display()

        with self.assertRaises(TypeError):
            d9 = Square(2.9)
            d9.display()

        with self.assertRaises(ValueError):
            dd2 = Square(2, -1, 1)
            dd2.display()

        with self.assertRaises(TypeError):
            dd3 = Square(3, 1, '0')
            dd3.display()

        with self.assertRaises(TypeError):
            dd5 = Square(5, [0], 1)
            dd5.display()

        with self.assertRaises(TypeError):
            dd6 = Square(4, (1, 0), 2)
            dd6.display()

        with self.assertRaises(TypeError):
            dd7 = Square(6, [7, 2], 4)
            dd7.display()

        with self.assertRaises(TypeError):
            dd8 = Square(1, '2', 2)
            dd8.display()

        with self.assertRaises(TypeError):
            dd9 = Square(4, 2, 2.9)
            dd9.display()


    '''=====================str=========================='''
    def test_Str(self):
        re = Square(10, 30, 2, 3)
        ex_out = "[Square] ({}) 30/2 - 10".format(re.id)
        self.assertEqual(str(re), ex_out)

        re1 = Square(10, 30, 3)
        ex_out = "[Square] ({}) 30/3 - 10".format(re1.id)
        self.assertEqual(str(re1), ex_out)

        with self.assertRaises(TypeError):
            re2 = Square(4, '2', 2)
            re2.__str__()

        with self.assertRaises(TypeError):
            re3 = Square(1, 2, 2.9)
            re3.__str__()

        with self.assertRaises(ValueError):
            re4 = Square(2, -1, 1)
            re4.__str__()

        with self.assertRaises(TypeError):
            re5 = Square(9, 1, '0')
            re5.__str__()

        with self.assertRaises(TypeError):
            re6 = Square(5, [0], 1)
            re6._str()

        with self.assertRaises(TypeError):
            re7 = Square(4, (1, 0), 2)
            re7.__str__()

        with self.assertRaises(TypeError):
            re8 = Square(6, [7, 2], 4)
            re8.__str__()


    '''=====================update=========================='''
    def test_update(self):
        up = Square(10, 7, 2, 3)
        up_k = Square(10, 7, 2, 3)

        up.update(100, 5, 6, 0)
        self.assertEqual(up.size, 5)
        self.assertEqual(up.x, 6)
        self.assertEqual(up.y, 0)
        self.assertEqual(up.id, 100)

        up_k.update(id=70, size=15)
        self.assertEqual(up_k.x, 7)
        self.assertEqual(up_k.y, 2)
        self.assertEqual(up_k.size, 15)
        self.assertEqual(up_k.id, 70)

        up2 = Square(10)
        up2.update(100, 6, (0), 0)
        self.assertEqual(up2.x, 0)
        self.assertEqual(up2.y, 0)
        self.assertEqual(up2.size, 6)
        self.assertEqual(up2.id, 100)

        up_k2 = Square(10)
        up_k2.update(id=10, size=8, x=(2), y=3)
        self.assertEqual(up_k2.size, 8)
        self.assertEqual(up_k2.x, 2)
        self.assertEqual(up_k2.y, 3)
        self.assertEqual(up_k2.id, 10)

        with self.assertRaises(TypeError):
            up.update(100, [5], 6, 0)

        with self.assertRaises(ValueError):
            up.update(100, -5, 6, 0)

        with self.assertRaises(TypeError):
            up.update(100, 5, '6', 0)

        with self.assertRaises(TypeError):
            up.update(100, (5, 6))

        with self.assertRaises(TypeError):
            up.update(100, [5, 0], 6, 0)

        with self.assertRaises(TypeError):
            up_k.update(id=100, size=[5])

        with self.assertRaises(ValueError):
            up_k.update(id=100, size=-6)

        with self.assertRaises(TypeError):
            up_k.update(id=100, size='5')

        with self.assertRaises(TypeError):
            up_k.update(id=100, size=(5, 6))

        with self.assertRaises(TypeError):
            up_k.update(id=100, size=[5, 0], x= 0)



if __name__ == '__main__':
    unittest.main
