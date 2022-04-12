import random
import prompt


def generate_expression():
    num_1 = random.randint(1, 25)
    num_2 = random.randint(1, 25)
    rand_ops = ['+', '-', '*']
    return f'{num_1} {random.choice(rand_ops)} {num_2}'


def run_brain_calc():
    print('Welcome to the Brain Games!')
    player = prompt.string("May I have your name? ")
    print("Hello, " + player)
    print('What is the result of this expression?')
    index = 0
    while index < 3:
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
    print("Congratulations, " + player + "!")
