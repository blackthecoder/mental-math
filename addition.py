from random import randrange


def random_two_of_one_digit_number_for_addition():
    first = randrange(1, 9)
    second = randrange(1, 9)
    summed = first + second
    return first, second, summed


def main():
    while True:
        first, second, summed = random_two_of_one_digit_number_for_addition()
        while True:
            guess = int(input(f'{first} + {second} = ?: '))
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
