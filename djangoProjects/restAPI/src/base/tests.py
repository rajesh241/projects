"""
Module for testing
"""
from django.test import TestCase

from base.calc import add


class CalcTests(TestCase):
    """
    Test class to check functions in calc module
    """
    def test_add_numbers(self):
        """
        Test case for testing addition of numbers
        """
        self.assertEqual(add(3, 8), 11)
