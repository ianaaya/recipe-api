from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        result = calc.add(7,9)
        self.assertEqual(result, 16)


    def test_subtract_numbers(self):
        result = calc.subtract(4, 15)
        self.assertEqual(result, 11)