import random


def generate_expression():
    num_1 = random.randint(1, 25)
    num_2 = random.randint(1, 25)
    rand_ops = ['+', '-', '*']
    return f'{num_1} {random.choice(rand_ops)} {num_2}'


def ask_question():
    global expression
    expression = generate_expression()
    print('Question: ' + expression)


def get_correct_answer():
    correct_answer = str(eval(expression))
    return correct_answer
