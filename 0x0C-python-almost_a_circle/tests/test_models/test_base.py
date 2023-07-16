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


class TestRectangle(unittest.TestCase):
    '''testing Rectangle'''
    def test_RectangleInitialized(self):
        rec = Rectangle(10, 20, 2, 3, 6)
        self.assertEqual(rec.id, 6)
        self.assertEqual(rec.width, 10)
        self.assertEqual(rec.height, 20)
        self.assertEqual(rec.x, 2)
        self.assertEqual(rec.y, 3)
       
    def test_RectangleSetter(self):
        Set = Rectangle(10, 20, 2, 3)
        Set.width = 11
        Set.height = 15
        Set.x = 4
        Set.y = 1
        self.assertEqual(Set.width, 11)
        self.assertEqual(Set.height, 15)
        self.assertEqual(Set.x, 4)
        self.assertEqual(Set.y, 1)


    '''=====================testing for validation======================'''
    def test_RectangleValidation(self):

        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -6)

        with self.assertRaises(ValueError):
            r2 = Rectangle(0, 0)

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

        with self.assertRaises(TypeError):
            r10 = Rectangle("6", 2, 0, 0, 5)

        with self.assertRaises(TypeError):
            r11 = Rectangle(6, 5, 0, (1, 2))
        
        with self.assertRaises(Exception):
            r12 = Rectangle()

        with self.assertRaises(ValueError):
            r13 = Rectangle(5, )

    '''================testing for area=========================='''
    def test_RectangleArea(self):
        a1 = Rectangle(2, 6)
        self.assertEqual(a1.area(), 12)

        a2 = Rectangle(2, 2, 0, 0, 5)
        self.assertEqual(a2.area(), 4)

        a3 = Rectangle(3, (5), 0, 1)
        self.assertEqual(a3.area(), 15)

        with self.assertRaises(ValueError):
            a4 = Rectangle(0, 0)
            a4.area()
        with self.assertRaises(ValueError):
            a4 = Rectangle(1, -6)
            a4.area()

        with self.assertRaises(ValueError):
            a5 = Rectangle(0, 6)
            a5.area()

        with self.assertRaises(TypeError):
            a6 = Rectangle(4, [5])
            a6.area()

        with self.assertRaises(Exception):
            a7 = Rectangle(5)
            a7.area()

        with self.assertRaises(Exception):
            a8 = Rectangle()
            a8.area()

        with self.assertRaises(TypeError):
            a9 = Rectangle(9, 5, [0, 1])
            a9.area()

        with self.assertRaises(ValueError):
            a10 = Rectangle(2, 5, 0, -1)
            a10.area()

        with self.assertRaises(TypeError):
            a11 = Rectangle(5, 5, 0.2, 1)
            a11.area()

        with self.assertRaises(TypeError):
            a12 = Rectangle("6", 2, 0, 0, 5)
            a12.area()

        with self.assertRaises(TypeError):
            a13 = Rectangle(6, 5, 0, (1, 2))
            a13.area()
        
        with self.assertRaises(Exception):
            a14 = Rectangle()
            a14.area()

        with self.assertRaises(ValueError):
            a15 = Rectangle(5, )
            a15.area()


    '''=============testing for display `#` a output========================'''
    def test_RectangleDisplay(self):
        import io
        from unittest.mock import patch
        d = Rectangle(2, 3)
        output = '##\n##\n##\n'
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            d.display()
            self.assertEqual(fake_stdout.getvalue(), output)

        d1 = Rectangle((2), 3)
        outp = '##\n##\n##\n'
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            d1.display()
            self.assertEqual(fake_stdout.getvalue(), outp)

        dd1 = Rectangle(2, 3, 0, (1))
        outp1 = '\n##\n##\n##\n'
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            dd1.display()
            self.assertEqual(fake_stdout.getvalue(), outp1)

        dd2 = Rectangle((2), 3, 0, 0)
        outp2 = '##\n##\n##\n'
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            dd2.display()
            self.assertEqual(fake_stdout.getvalue(), outp2)

        with self.assertRaises(ValueError):
            d2 = Rectangle(2, 0)
            d2.display()

        with self.assertRaises(ValueError):
            d3 = Rectangle(0, 0)
            d3.display()

        with self.assertRaises(ValueError):
            d4 = Rectangle(-2, 2)
            d4.display()

        with self.assertRaises(TypeError):
            d5 = Rectangle(3, [5], 0, 1)
            d5.display()

        with self.assertRaises(TypeError):
            d6 = Rectangle((2, 4), 2)
            d6.display()

        with self.assertRaises(TypeError):
            d7 = Rectangle(2, [7, 2])
            d7.display()

        with self.assertRaises(TypeError):
            d8 = Rectangle('2', 2)
            d8.display()

        with self.assertRaises(TypeError):
            d9 = Rectangle(2, 2.9)
            d9.display()

        with self.assertRaises(ValueError):
            dd2 = Rectangle(2, 1, -1, 1)
            dd2.display()

        with self.assertRaises(TypeError):
            dd3 = Rectangle(3, 9, 1, '0')
            dd3.display()

        with self.assertRaises(TypeError):
            dd5 = Rectangle(3, 5, [0], 1)
            dd5.display()

        with self.assertRaises(TypeError):
            dd6 = Rectangle(2, 4, (1, 0), 2)
            dd6.display()

        with self.assertRaises(TypeError):
            dd7 = Rectangle(2, 6, [7, 2], 4)
            dd7.display()

        with self.assertRaises(TypeError):
            dd8 = Rectangle(4, 1, '2', 2)
            dd8.display()

        with self.assertRaises(TypeError):
            dd9 = Rectangle(4, 1, 2, 2.9)
            dd9.display()


    '''=====================str=========================='''
    def test_Str(self):
        re = Rectangle(10, 30, 2, 3)
        ex_out = "[Rectangle] ({}) 2/3 - 10/30".format(re.id)
        self.assertEqual(str(re), ex_out)

        re1 = Rectangle(10, 30)
        ex_out = "[Rectangle] ({}) 0/0 - 10/30".format(re1.id)
        self.assertEqual(str(re1), ex_out)

        with self.assertRaises(TypeError):
            re2 = Rectangle(4, 1, '2', 2)
            re2.__str__()

        with self.assertRaises(TypeError):
            re3 = Rectangle(4, 1, 2, 2.9)
            re3.__str__()

        with self.assertRaises(ValueError):
            re4 = Rectangle(2, 1, -1, 1)
            re4.__str__()

        with self.assertRaises(TypeError):
            re5 = Rectangle(3, 9, 1, '0')
            re5.__str__()

        with self.assertRaises(TypeError):
            re6 = Rectangle(3, 5, [0], 1)
            re6._str()

        with self.assertRaises(TypeError):
            re7 = Rectangle(2, 4, (1, 0), 2)
            re7.__str__()

        with self.assertRaises(TypeError):
            re8 = Rectangle(2, 6, [7, 2], 4)
            re8.__str__()


    '''=====================update=========================='''
    def test_update(self):
        up = Rectangle(10, 30, 17, 2, 3)
        up_k = Rectangle(10, 30, 17, 2, 3)

        up.update(100, 5, 6, 0)
        self.assertEqual(up.width, 5)
        self.assertEqual(up.x, 0)
        self.assertEqual(up.y, 2)
        self.assertEqual(up.height, 6)
        self.assertEqual(up.id, 100)

        up_k.update(id=70, width=15, height=16)
        self.assertEqual(up_k.width, 15)
        self.assertEqual(up_k.x, 17)
        self.assertEqual(up_k.y, 2)
        self.assertEqual(up_k.height, 16)
        self.assertEqual(up_k.id, 70)

        up2 = Rectangle(10, 30)
        up2.update(100, 5, 6, (0), 0)
        self.assertEqual(up2.width, 5)
        self.assertEqual(up2.x, 0)
        self.assertEqual(up2.y, 0)
        self.assertEqual(up2.height, 6)
        self.assertEqual(up2.id, 100)

        up_k2 = Rectangle(10, 30)
        up_k2.update(id=10, width=8, height=14, x=(2), y=3)
        self.assertEqual(up_k2.width, 8)
        self.assertEqual(up_k2.x, 2)
        self.assertEqual(up_k2.y, 3)
        self.assertEqual(up_k2.height, 14)
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
            up_k.update(id=100, width=[5], height=6)

        with self.assertRaises(ValueError):
            up_k.update(id=100, width=5, height=-6)

        with self.assertRaises(TypeError):
            up_k.update(id=100, width='5', height=6)

        with self.assertRaises(TypeError):
            up_k.update(id=100, width=(5, 6), height=6)

        with self.assertRaises(TypeError):
            up_k.update(id=100, width=[5, 0], height=6, x= 0)



if __name__ == '__main__':
    unittest.main
