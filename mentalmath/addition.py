from random import randrange
from mentalmath.interface import guessing


def random_two_of_one_digit_number_for_addition():
    first_number = randrange(1, 9)
    second_number = randrange(1, 9)
    summed = first_number + second_number
    return first_number, second_number, summed


def main():
    guessing(random_two_of_one_digit_number_for_addition, '+')


if __name__ == '__main__':
    main()
