#!/usr/bin/python3
"""Defines test classes for Base class"""

import unittest
from io import StringIO
import os
from unittest.mock import patch
from models.base import Base


class TestBase(unittest.TestCase):
    def test_assigning_automatically_id(self):
        self.assertEqual(Base().id, 1)

    # Other test cases for Base class


if __name__ == '__main__':
    unittest.main()
