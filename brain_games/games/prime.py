from math import sqrt
from random import randint

GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    # prime numbers not included in the loop
    if number == 2 or number == 3 or number == 5 or number == 7:
        return True
    # using trial division method to define whether the number is prime
    else:
        number_sqrt = int(sqrt(number))
        for divisor in range(2, number_sqrt + 1):
            if number % divisor == 0:
                return False
        return True


def get_question_and_answer():
    question = randint(1, 100)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, correct_answer
