import prompt
from .games import even, gcd, calc, prime, progression


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
        even.ask_question()
    elif game == 'gcd':
        gcd.ask_question()
    elif game == 'calc':
        calc.ask_question()
    elif game == 'prime':
        prime.ask_question()
    elif game == 'progression':
        progression.ask_question()


def get_correct_answer(game):
    if game == 'even':
        correct_answer = even.get_correct_answer()
        return correct_answer
    elif game == 'gcd':
        correct_answer = gcd.get_correct_answer()
        return correct_answer
    elif game == 'calc':
        correct_answer = calc.get_correct_answer()
        return correct_answer
    elif game == 'prime':
        correct_answer = prime.get_correct_answer()
        return correct_answer
    elif game == 'progression':
        correct_answer = progression.get_correct_answer()
        return correct_answer


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
