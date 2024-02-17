import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    def test_base__init__(self):
        """Test the id attribute of the Base class"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_create(self):
        """Test the create method of the Base class"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        self.assertIsInstance(r2, Rectangle)
        # self.assertEqual(r1, r2)

        self.assertIsNot(r1, r2)

    def test_save_to_file(self):
        """Test the save_to_file method of the Base class"""
        pass

    # def test_load_from_file(cls):


if __name__ == '__main__':
    unittest.main()
