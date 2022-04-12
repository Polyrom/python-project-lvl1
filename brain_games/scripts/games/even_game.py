import prompt
from random import randint


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def run_brain_even():
    print('Welcome to the Brain Games!')
    player = prompt.string("May I have your name? ")
    print("Hello, " + player)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    index = 0
    while index < 3:
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
    print("Congratulations, " + player + "!")
