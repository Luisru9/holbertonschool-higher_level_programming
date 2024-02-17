#!/usr/bin/python3
"""Unittests for Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def test_id(self):
        """Test id assignment"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)
        b5 = Base(0)
        self.assertEqual(b5.id, 0)

    def test_no_args(self):
        """Test with no arguments"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_none_id(self):
        """Test with None as id"""
        b = Base(None)
        self.assertEqual(b.id, 1)

    def test_str(self):
        """Test __str__ method"""
        b = Base(42)
        self.assertEqual(str(b), "[Base] (42)")


if __name__ == "__main__":
    unittest.main()
