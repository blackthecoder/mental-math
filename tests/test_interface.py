import unittest
from unittest.mock import patch
from mentalmath.interface import display_question_and_return_number_from_user, GUESSING_TEMPLATE


class TestInterface(unittest.TestCase):

    @patch('builtins.input', return_value='10')
    def test_type_valid_number_to_guessing(self, mock_input):
        first_number = '10'
        second_number = '16'
        operator = '+'
        display_question_and_return_number_from_user(first_number, second_number, operator)
        mock_input.assert_called_with(GUESSING_TEMPLATE.format(first_number=first_number,
                                      second_number=second_number, operator=operator))

    def test_get_exception_when_type_invalid_number_to_guessing(self):
        with patch('builtins.input', return_value='a'):
            self.assertRaises(ValueError, display_question_and_return_number_from_user, '10', '10', '+')


if __name__ == '__main__':
    unittest.main()
