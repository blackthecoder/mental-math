import unittest
from unittest.mock import patch
from mentalmath.interface import display_question_and_return_number_from_user


class TestInterface(unittest.TestCase):

    def test_type_valid_number_to_display_question_and_return_number_from_user(self):
        with patch('builtins.input', return_value='10'):
            display_question_and_return_number_from_user('10', '10', '+')

    def test_get_exception_when_type_invalid_number_to_display_question_and_return_number_from_user(self):
        with patch('builtins.input', return_value='a'):
            self.assertRaises(ValueError, display_question_and_return_number_from_user, '10', '10', '+')


if __name__ == '__main__':
    unittest.main()
