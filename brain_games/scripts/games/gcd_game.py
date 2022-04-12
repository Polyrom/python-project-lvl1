import prompt
from random import randint
from math import gcd


def sample_numbers(number_1, number_2):
    return f'{number_1} {number_2}'


def run_brain_gcd():
    print('Welcome to the Brain Games!')
    player = prompt.string("May I have your name? ")
    print("Hello, " + player)
    print('Find the greatest common divisor of given numbers.')
    index = 0
    while index < 3:
        number_1 = randint(1, 99)
        number_2 = randint(1, 99)
        numbers = sample_numbers(number_1, number_2)
        print('Question: ' + numbers)
        answer = prompt.integer("Your answer: ")
        correct_answer = gcd(number_1, number_2)
        if answer == correct_answer:
            print("Correct!")
            index += 1
        else:
            return print(
                f'"{answer}" is wrong answer ;(. '
                f'The correct answer was "{correct_answer}".'
                f'\nLet\'s try again, {player}!')

    print("Congratulations, " + player + "!")
