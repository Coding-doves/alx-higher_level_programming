import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

'''testcase for JSON

'''


class TestJson2(unittest.TestCase):
    '''testing Json'''
    def test_fromJson(self):
        '''from Json string'''
        with self.assertRaises(TypeError):
            rec = Rectangle.from_json_string([])

        json_dic = Rectangle.from_json_string(None)
        self.assertEqual(json_dic, '[]')

        list_input = [
            {'id': 8, 'width': 14, 'height': 9}, 
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        json_output = Rectangle.from_json_string(json_list_input)
        out = [{'id': 8, 'width': 14, 'height': 9}, {'id': 7, 'width': 1, 'height': 7}]
        self.assertEqual(json_output, out)

        s = '[{"id": 2, "size": 9, "x": 2, "y": 3}]'
        json_dic_sq = Square.to_json_string([s])
        out1 = '[{"id": 2, "size": 9, "x": 2, "y": 3}]'
        self.assertEqual(json_dic_sq, out1)
