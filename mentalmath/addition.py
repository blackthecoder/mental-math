from random import randrange
from mentalmath.interface import display_question_and_return_number_from_user


def random_two_of_one_digit_number_for_addition():
    first_number = randrange(1, 9)
    second_number = randrange(1, 9)
    summed = first_number + second_number
    return first_number, second_number, summed


def main():
    while True:
        first_number, second_number, summed = random_two_of_one_digit_number_for_addition()
        while True:
            guess = display_question_and_return_number_from_user(first_number, second_number, '+')
            if guess != summed:
                print('No!!!!!')
                continue
            break
        again = input('Nice!!!, Play again? ([y]/n): ')
        if len(again) == 0 or again.upper()[0] == 'Y':
            continue
        break
    print('Bye')


if __name__ == '__main__':
    main()
