from random import randint
from math import gcd


game_rules = 'Find the greatest common divisor of given numbers.'


def ask_question_get_answer():
    number_1, number_2 = randint(1, 99), randint(1, 99)
    question = f"{number_1}, {number_2}"
    correct_answer = str(gcd(number_1, number_2))
    return question, correct_answer
