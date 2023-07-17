import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

'''testcase for JSON

'''


class TestJson(unittest.TestCase):
    '''testing Json'''
    def test_To(self):
        rec = Base.to_json_string([])
        self.assertEqual(rec, '[]')

        json_dic = Base.to_json_string(None)
        self.assertEqual(json_dic, '[]')
       
        r = Rectangle(14, 9, 2, 3)
        dic = r.to_dictionary()
        json_dic1 = Base.to_json_string([dic])
        out = '[{"id": 1, "width": 14, "height": 9, "x": 2, "y": 3}]'
        self.assertEqual(json_dic1, out)

        r = Rectangle((14), 9, 2, 3)
        dic = r.to_dictionary()
        json_dic1 = Base.to_json_string([dic])
        out = '[{"id": 2, "width": 14, "height": 9, "x": 2, "y": 3}]'
        self.assertEqual(json_dic1, out)

        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 3, 9, 2)
            dic1 = r1.to_dictionary()

        with self.assertRaises(ValueError):
            r2 = Rectangle(1, -4)
            dic2 = r2.to_dictionary()

        with self.assertRaises(ValueError):
            r3 = Rectangle()
            dic3 = r3.to_dictionary()

        with self.assertRaises(TypeError):
            r4 = Rectangle(10, [3])
            dic4 = r4.to_dictionary()

        with self.assertRaises(TypeError):
            r5 = Rectangle(6, (3, 2))
            dic5 = r5.to_dictionary()

        with self.assertRaises(ValueError):
            r6 = Rectangle(0, 0)
            dic6 = r6.to_dictionary()

        s = Square(9, 2, 3)
        sq = s.to_dictionary()
        json_dic_sq = Base.to_json_string([sq])
        out = '[{"id": 9, "size": 9, "x": 2, "y": 3}]'
        self.assertEqual(json_dic_sq, out)

        s0 = Square(9, (2), 3)
        sq1 = s0.to_dictionary()
        json_dic_sq2 = Base.to_json_string([sq1])
        out = '[{"id": 10, "size": 9, "x": 2, "y": 3}]'
        self.assertEqual(json_dic_sq2, out)

        with self.assertRaises(ValueError):
            s1 = Square(0, 3, 9, 2)
            c1 = s1.to_dictionary()

        with self.assertRaises(ValueError):
            s2 = Square(1, -4)
            c2 = s2.to_dictionary()

        with self.assertRaises(TypeError):
            s3 = Square()
            c3 = s3.to_dictionary()

        with self.assertRaises(TypeError):
            s4 = Square(10, [3])
            c4 = s4.to_dictionary()

        with self.assertRaises(TypeError):
            s5 = Square(6, (3, 2))
            c5 = s5.to_dictionary()

        with self.assertRaises(ValueError):
            s6 = Square(0, 0)
            c6 = s6.to_dictionary()
