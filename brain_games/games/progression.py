from random import randint


GAME_RULES = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 8


def generate_progression(start, total_steps, difference):
    progression = [str(start)]
    i = 0
    while i <= total_steps:
        progression.append(str(start + difference))
        start += difference
        i += 1
    return progression


def get_question_and_answer():
    seq_start = randint(1, 5)
    step = randint(2, 5)
    progression_list = generate_progression(seq_start, PROGRESSION_LENGTH, step)
    random_index = randint(0, PROGRESSION_LENGTH)
    correct_answer = str(progression_list[random_index])
    progression_list[random_index] = '..'
    question = ' '.join(progression_list)
    return question, correct_answer
