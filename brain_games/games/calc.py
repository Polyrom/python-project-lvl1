import random
import operator


GAME_RULES = 'What is the result of the expression?'


def get_question_and_answer():
    operators = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul}
    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)
    operators_choice = random.choice(list(operators.keys()))
    question = '{} {} {}'.format(num1, operators_choice, num2)
    correct_answer = operators.get(operators_choice)(num1, num2)
    return question, correct_answer
