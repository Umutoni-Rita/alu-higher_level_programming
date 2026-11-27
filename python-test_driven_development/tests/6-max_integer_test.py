#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Max of an ascending list is the last element."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max of an unordered list is found."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Max at the first position is found."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """An empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """Calling with no argument returns None."""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """A single-element list returns that element."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Max of only negative numbers is the one closest to zero."""
        self.assertEqual(max_integer([-5, -1, -3]), -1)

    def test_mixed_signs(self):
        """Max of mixed positive and negative numbers is found."""
        self.assertEqual(max_integer([-10, 0, 10, -20]), 10)

    def test_duplicates(self):
        """Repeated max values still return the max."""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_floats(self):
        """Floats are compared correctly."""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_ints_and_floats(self):
        """A mix of ints and floats is compared correctly."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_string(self):
        """A string returns its highest character."""
        self.assertEqual(max_integer("Holberton"), "t")

    def test_list_of_strings(self):
        """A list of strings returns the alphabetically last one."""
        self.assertEqual(max_integer(["a", "abc", "b"]), "b")

    def test_none(self):
        """None raises a TypeError (it has no length)."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_mixed_types(self):
        """Comparing ints with strings raises a TypeError."""
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])


if __name__ == "__main__":
    unittest.main()
