#!/usr/bin/python3
'''
Testcase for JSON

'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestJson(unittest.TestCase):
    '''
    Testcase for JSON

    '''
    def test_to(self):
        '''testing Json'''
        rec = Base.to_json_string([])
        self.assertEqual(rec, '[]')

        json_dic = Base.to_json_string(None)
        self.assertEqual(json_dic, '[]')
       
        r_s = Rectangle(14, 9, 2, 3)
        dic = r_s.to_dictionary()
        json_dic1 = Base.to_json_string([dic])
        out = f'[{{"id": {r_s.id}, "width": 14, "height": 9, "x": 2, "y": 3}}]'
        self.assertEqual(json_dic1, out)

        r_ss = Rectangle((14), 9, 2, 3)
        dic = r_ss.to_dictionary()
        json_dic1 = Base.to_json_string([dic])
        out = f'[{{"id": {r_ss.id}, "width": 14, "height": 9, "x": 2, "y": 3}}]'
        self.assertEqual(json_dic1, out)

        with self.assertRaises(ValueError):
            r_s1 = Rectangle(0, 3, 9, 2)
            r_s1.to_dictionary()

            r_s2 = Rectangle(1, -4)
            r_s2.to_dictionary()

            r_s3 = Rectangle()
            r_s3.to_dictionary()

            r_s6 = Rectangle(0, 0)
            r_s6.to_dictionary()

        with self.assertRaises(TypeError):
            r_s4 = Rectangle(10, [3])
            r_s4.to_dictionary()
            r_s5 = Rectangle(6, (3, 2))
            r_s5.to_dictionary()

        squ = Square(9, 2, 3, 7)
        sq_d = squ.to_dictionary()
        json_dic_sq = Base.to_json_string([sq_d])
        out = f'[{{"id": {squ.id}, "size": 9, "x": 2, "y": 3}}]'
        self.assertEqual(json_dic_sq, out)

        squ0 = Square(9, (2), 3, 8)
        sq_d1 = squ0.to_dictionary()
        json_dic_sq2 = Base.to_json_string([sq_d1])
        out = f'[{{"id": {squ0.id}, "size": 9, "x": 2, "y": 3}}]'
        self.assertEqual(json_dic_sq2, out)

        with self.assertRaises(ValueError):
            squ1 = Square(0, 3, 9, 2)
            squ1.to_dictionary()

            squ2 = Square(1, -4)
            squ2.to_dictionary()

            squ6 = Square(0, 0)
            squ6.to_dictionary()

        with self.assertRaises(TypeError):
            squ3 = Square()
            squ3.to_dictionary()

            squ4 = Square(10, [3])
            squ4.to_dictionary()

            squ5 = Square(6, (3, 2))
            squ5.to_dictionary()


        if __name__ == '__main__':
            unittest.main()
