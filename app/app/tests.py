from django.test import TestCase
from app.calc import add, sub


class CalcTest(TestCase):
    def test_add_numbers(self):
        """test that two numbers are added together."""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        self.assertEqual(sub(8, 5), 3)
