import random
import operator


GAME_RULES = 'What is the result of the expression?'


def get_question_and_answer():
    operations = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul}
    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)
    operations_choice = random.choice(list(operations.keys()))
    question = f'{num1} {operations_choice} {num2}'
    random_func = operations.get(operations_choice)
    correct_answer = str(random_func(num1, num2))
    return question, correct_answer
