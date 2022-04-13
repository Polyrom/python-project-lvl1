from random import randint
from math import sqrt
import prompt


def is_prime(number):
    if number == 2 or number == 3 or number == 5 or number == 7:
        return 'yes'
    else:
        number_sqrt = int(sqrt(number))
        i = 2
        while i <= (number_sqrt + 1):
            if number % i == 0:
                return 'no'
            else:
                i += 1
        return 'yes'


def run_brain_prime():
    print('Welcome to the Brain Games!')
    player = prompt.string("May I have your name? ")
    print("Hello, " + player)
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    index = 0
    while index < 3:
        num = randint(1, 100)
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        correct_answer = is_prime(num)
        if answer == correct_answer:
            print("Correct!")
            index += 1
        else:
            return print(
                f'"{answer}" is wrong answer ;(. '
                f'The correct answer was "{correct_answer}".'
                f'\nLet\'s try again, {player}!')
    print("Congratulations, " + player + "!")
