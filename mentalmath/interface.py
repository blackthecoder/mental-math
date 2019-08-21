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


def guessing(question_generator, operator):
    while True:
        first_number, second_number, result = question_generator()
        while True:
            guess = display_question_and_return_number_from_user(first_number, second_number, operator)
            if guess != result:
                print('No!!!!!')
                continue
            break
        again = input('Nice!!!, Play again? ([y]/n): ')
        if len(again) == 0 or again.upper()[0] == 'Y':
            continue
        break
    print('Bye')
