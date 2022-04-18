from random import randint


number = randint(1, 99)


def is_even(num):
    return 'yes' if num % 2 == 0 else 'no'
