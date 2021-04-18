from unittest import TestCase

from gender_converter import convert_gender


class Test(TestCase):
    def test_convert_gender(self):
        actual = convert_gender("M")
        expected = "MALE"
        self.assertEqual(actual, expected)