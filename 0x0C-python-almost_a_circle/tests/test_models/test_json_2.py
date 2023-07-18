#!/usr/bin/python3
'''
Testcase for JSON

'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestJson2(unittest.TestCase):
    '''
    Testcase for JSON

    '''
    def test_from_json(self):
        '''from Json string'''
        with self.assertRaises(TypeError):
            rec = Base.from_json_string([])

        json_dic = Base.from_json_string(None)
        self.assertEqual(json_dic, '[]')

        list_input = '[{"d" 8, "width" 14, "height" 9}]'

        json_output = Base.from_json_string(list_input)
        out = '[{"id": 8, "width": 14, "height": 9}]'
        self.assertEqual(json_output, out)

        s = '[{"id": 2, "size": 9, "x": 2, "y": 3}]'
        json_dic_sq = Base.to_json_string([s])
        out1 = '[{"id": 2, "size": 9, "x": 2, "y": 3}]'
        self.assertEqual(json_dic_sq, out1)

        if __name__ == '__main__':
            unittest.main()
