#!/usr/bin/python3
"""Unittests for base
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Define unittest for Base models"""

    def test_initialization(self):
        base_1 = Base()
        base_2 = Base()
        self.assertEqual(base_1.id, 1)
        self.assertEqual(base_2.id, 2)

    def test_saving_id(self):
        base = Base(100)
        self.assertEqual(base.id, 100)

    def test_to_json_string_valid(self):
        pass

if __name__ == '__main__':
    unittest.main()