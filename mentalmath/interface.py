def display_question_and_return_number_from_user(first_number, second_number, operator):
    while True:
        try:
            guess = int(input(f'{first_number} {operator} {second_number} = ?: '))
            return guess
        except ValueError as e:
            print('Please type a valid number !!!')
            continue
