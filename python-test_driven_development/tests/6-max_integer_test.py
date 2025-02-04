#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_ordered_list(self):
        """Test an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test that an empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test a list with one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_all_negative(self):
        """Test a list of all negative numbers."""
        self.assertEqual(max_integer([-10, -3, -1, -20]), -1)

    def test_mixed_numbers(self):
        """Test a list with mixed positive and negative numbers."""
        self.assertEqual(max_integer([-10, 0, 10, -20]), 10)

    def test_duplicates(self):
        """Test a list with duplicate maximum values."""
        self.assertEqual(max_integer([1, 2, 4, 4, 3]), 4)

    def test_floats(self):
        """Test a list of float numbers."""
        self.assertEqual(max_integer([1.5, 2.3, 2.2]), 2.3)

    def test_ints_and_floats(self):
        """Test a list with both integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 3, 2.7]), 3)

if __name__ == '__main__':
    unittest.main()
