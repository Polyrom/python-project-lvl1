from random import randint


def is_even(num):
    return 'yes' if num % 2 == 0 else 'no'


def ask_question():
    global number
    number = randint(1, 99)
    print(f'Question: {number}')


def get_correct_answer():
    correct_answer = is_even(number)
    return correct_answer
