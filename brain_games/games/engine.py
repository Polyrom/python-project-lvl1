import prompt
from random import randint
from math import gcd
from .even import is_even
from .gcd import sample_numbers
from .calc import generate_expression
from .prime import is_prime
from .progression import get_progression


def explain_how_to_answer(game):
    if game == 'even':
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif game == 'gcd':
        print('Find the greatest common divisor of given numbers.')
    elif game == 'calc':
        print('What is the result of this expression?')
    elif game == 'prime':
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
    elif game == 'progression':
        print('What number is missing in the progression?')


def show_question(game):
    if game == 'even':
        global number
        number = randint(1, 99)
        print(f'Question: {number}')
    elif game == 'gcd':
        global number_1, number_2
        number_1, number_2 = randint(1, 99), randint(1, 99)
        numbers = sample_numbers(number_1, number_2)
        print('Question: ' + numbers)
    elif game == 'calc':
        global expression
        expression = generate_expression()
        print('Question: ' + expression)
    elif game == 'prime':
        global num
        num = randint(1, 100)
        print(f'Question: {num}')
    elif game == 'progression':
        seq_start = randint(1, 5)
        step = randint(2, 5)
        num_of_steps = 8
        progression_list = get_progression(seq_start, num_of_steps, step)
        secret_number = randint(0, 8)
        global cor_ans
        cor_ans = str(progression_list[secret_number])
        progression_list[secret_number] = '..'
        question_string = ' '.join(str(e) for e in progression_list)
        print(f'Question: {question_string}')


def get_correct_answer(game):
    if game == 'even':
        correct_answer = is_even(number)
        return correct_answer
    elif game == 'gcd':
        correct_answer = str(gcd(number_1, number_2))
        return correct_answer
    elif game == 'calc':
        correct_answer = str(eval(expression))
        return correct_answer
    elif game == 'prime':
        correct_answer = is_prime(num)
        return correct_answer
    elif game == 'progression':
        return cor_ans


def run_game(game):
    print('Welcome to the Brain Games!')
    player = prompt.string('May I have your name? ')
    print('Hello, ' + player)
    explain_how_to_answer(game)
    index = 0
    while index < 3:
        show_question(game)
        answer = prompt.string('Your answer: ')
        if answer == get_correct_answer(game):
            print('Correct!')
            index += 1
        else:
            return print(
                f'"{answer}" is wrong answer ;(. '
                f'The correct answer was "{get_correct_answer(game)}".'
                f'\nLet\'s try again, {player}!')
    print("Congratulations, " + player + "!")
