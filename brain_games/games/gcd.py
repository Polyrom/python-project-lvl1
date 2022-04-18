from random import randint
from math import gcd


def sample_numbers(number_1, number_2):
    return f'{number_1} {number_2}'


def ask_question():
    global number_1, number_2
    number_1, number_2 = randint(1, 99), randint(1, 99)
    numbers = sample_numbers(number_1, number_2)
    print('Question: ' + numbers)


def get_correct_answer():
    correct_answer = str(gcd(number_1, number_2))
    return correct_answer
