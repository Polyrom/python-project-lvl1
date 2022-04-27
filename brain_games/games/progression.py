from random import randint


GAME_RULES = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 8


def get_progression(start, total_steps, difference):
    progression = [start]
    i = 0
    while i <= total_steps:
        progression.append(start + difference)
        start = start + difference
        i += 1
    return progression


def get_question_and_answer():
    seq_start = randint(1, 5)
    step = randint(2, 5)
    progression_list = get_progression(seq_start, PROGRESSION_LENGTH, step)
    random_number = randint(0, 8)
    correct_answer = str(progression_list[random_number])
    progression_list[random_number] = '..'
    question = ' '.join(str(e) for e in progression_list)
    return question, correct_answer
