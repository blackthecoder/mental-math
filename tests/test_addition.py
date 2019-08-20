import unittest
from mentalmath.addition import random_two_of_one_digit_number_for_addition


class TestAddition(unittest.TestCase):

    def test_random_two_of_one_digit_number_for_addition(self):
        first, second, summed = random_two_of_one_digit_number_for_addition()
        self.assertEqual(first + second, summed)


if __name__ == '__main__':
    unittest.main()
