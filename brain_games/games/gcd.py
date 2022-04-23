from random import randint
from math import gcd


GAME_RULES = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    number_1, number_2 = randint(1, 99), randint(1, 99)
    question = f"{number_1} {number_2}"
    correct_answer = str(gcd(number_1, number_2))
    return question, correct_answer
