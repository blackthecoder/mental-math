GUESSING_TEMPLATE = '{first_number} {operator} {second_number} = ?: '


def display_question_and_return_number_from_user(first_number, second_number, operator):
    for i in range(3):
        try:
            guess = int(input(GUESSING_TEMPLATE.format(first_number=first_number, second_number=second_number,
                                                       operator=operator)))
            return guess
        except ValueError as e:
            print('Please type a valid number !!!')
            continue
    raise ValueError('Please type a valid number !!!')
