from random import randint


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def get_question_and_answer():
    question = randint(1, 99)
    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer
