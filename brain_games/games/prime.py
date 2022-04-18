from math import sqrt
from random import randint


def is_prime(number):
    # prime numbers not included in the loop
    if number == 2 or number == 3 or number == 5 or number == 7:
        return 'yes'
    # using trial division method to define whether the number is prime
    else:
        number_sqrt = int(sqrt(number))
        i = 2
        while i <= (number_sqrt + 1):
            if number % i == 0:
                return 'no'
            else:
                i += 1
        return 'yes'


def ask_question():
    global num
    num = randint(1, 100)
    print(f'Question: {num}')


def get_correct_answer():
    correct_answer = is_prime(num)
    return correct_answer
