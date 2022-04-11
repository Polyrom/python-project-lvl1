import prompt
from random import randint
from math import gcd
from .even_game import is_even
from .calc_game import generate_expression
from .gcd_game import sample_numbers


def ask_question(game):
    if game == 'even':
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif game == 'calc':
        print('What is the result of this expression?')
    elif game == 'gcd':
        print('Find the greatest common divisor of given numbers.')


def run_game(game):
    print('Welcome to the Brain Games!')
    player = prompt.string("May I have your name? ")
    print("Hello, " + player)
    ask_question(game)
    index = 0
    while index < 3:
        if game == 'even':
            number = randint(1, 99)
            print(f'Question: {number}')
            answer = prompt.string('Your answer: ')
            correct_answer = is_even(number)
            if answer == correct_answer:
                print("Correct!")
                index += 1
            else:
                return print(
                    f'"{answer}" is wrong answer ;(. '
                    f'The correct answer was "{correct_answer}".'
                    f'\nLet\'s try again, {player}!')
        elif game == 'calc':
            expression = generate_expression()
            print('Question: ' + expression)
            answer = prompt.integer("Your answer: ")
            correct_answer = eval(expression)
            if answer == correct_answer:
                print("Correct!")
                index += 1
            else:
                return print(
                    f'"{answer}" is wrong answer ;(. '
                    f'The correct answer was "{correct_answer}".'
                    f'\nLet\'s try again, {player}!')
        elif game == "gcd":
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
