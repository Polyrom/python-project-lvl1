import random


GAME_RULES = 'What is the result of the expression?'


def generate_expression():
    num_1 = random.randint(1, 25)
    num_2 = random.randint(1, 25)
    rand_ops = ['+', '-', '*']
    return f'{num_1} {random.choice(rand_ops)} {num_2}'


def change_str_to_expression(equation):
    if '+' in equation:
        y = equation.split('+')
        x = int(y[0]) + int(y[1])
    elif '-' in equation:
        y = equation.split('-')
        x = int(y[0]) - int(y[1])
    elif '*' in equation:
        y = equation.split('*')
        x = int(y[0]) * int(y[1])
    return x


def get_question_and_answer():
    question = generate_expression()
    correct_answer = str(change_str_to_expression(question))
    return question, correct_answer
