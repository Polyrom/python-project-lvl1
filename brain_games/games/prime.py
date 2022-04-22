from math import sqrt
from random import randint

game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    # prime numbers not included in the loop
    if number == 2 or number == 3 or number == 5 or number == 7:
        return True
    # using trial division method to define whether the number is prime
    else:
        number_sqrt = int(sqrt(number))
        i = 2
        while i <= (number_sqrt + 1):
            if number % i == 0:
                return False
            else:
                i += 1
        return True


def ask_question_get_answer():
    question = randint(1, 100)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, correct_answer
