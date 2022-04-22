import random


game_rules = 'What is the result of the expression?'


def generate_expression():
    num_1 = random.randint(1, 25)
    num_2 = random.randint(1, 25)
    rand_ops = ['+', '-', '*']
    return f'{num_1} {random.choice(rand_ops)} {num_2}'


def ask_question_get_answer():
    question = generate_expression()
    correct_answer = str(eval(question))
    return question, correct_answer
