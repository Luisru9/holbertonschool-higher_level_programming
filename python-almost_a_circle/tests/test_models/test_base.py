#!/usr/bin/python3
"""unittests for base.py"""
import os
from typing import Type
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """TestBase"""

    def test_zero_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_no_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)


class TestBase_to_json_string(unittest.TestCase):
    """Test Base"""

    def test_to_json_string_rectrangle_type(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        self.assertEqual(str, type(
            Base.to_json_string([rect.to_dictionary()])))

    def test_to_json_string_square_type(self):
        sq = Square(5, 4, 3, 2)
        self.assertEqual(str, type(Base.to_json_string([sq.to_dictionary()])))


class TestBase_save_to_file(unittest.TestCase):
    """Test Base"""

    def test_save_to_file_rectangle(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        Rectangle.save_to_file([rect])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read())) == 53

    def test_save_to_file_square(self):
        sq = Square(5, 4, 3, 2)
        Square.save_to_file([sq])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read())) == 39

    def save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """Test Base"""

    def test_from_json_string_rectangle(self):
        list = [{"id": 5, "width": 4, "height": 3, "x": 2, "y": 1}]
        input = Rectangle.to_json_string(list)
        output = Rectangle.from_json_string(input)
        self.assertEqual(list, output)

    def test_from_json_string_square(self):
        list = [{"id": 5, "size": 4, "x": 2, "y": 1}]
        input = Square.to_json_string(list)
        output = Square.from_json_string(input)
        self.assertEqual(list, output)

    def test_from_json_string_empty(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))


class TestBase_create(unittest.TestCase):
    """Test Base"""

    def test_create_rectangle(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect_dict = rect.to_dictionary()
        created_rect = Rectangle.create(**rect_dict)
        self.assertEqual("[Rectangle] (1) 3/2 - 5/4", str(rect))

    def test_create_square(self):
        sq = Square(5, 4, 3, 2)
        sq_dict = sq.to_dictionary()
        created_sq = Square.create(**sq_dict)
        self.assertEqual("[Square] (2) 4/3 - 5", str(sq))


class TestBase_load_from_file(unittest.TestCase):
    """Test Base"""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_rectangle(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect2 = Rectangle(6, 7, 8, 9, 0)
        Rectangle.save_to_file([rect, rect2])
        rect_list = Rectangle.load_from_file()
        self.assertEqual(str(rect2), str(rect_list[1]))

    def test_load_from_file_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_square(self):
        sq = Square(5, 4, 3, 2)
        sq2 = Square(6, 7, 8, 9)
        Square.save_to_file([sq, sq2])
        sq_list = Square.load_from_file()
        self.assertEqual(str(sq2), str(sq_list[1]))

    def test_load_from_file_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


if __name__ == '__main__':
    unittest.main()
