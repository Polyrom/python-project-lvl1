from random import randint


game_rules = 'What number is missing in the progression?'


def get_progression(start, total_steps, difference):
    progression = [start]
    i = 0
    while i <= total_steps:
        progression.append(start + difference)
        start = start + difference
        i += 1
    return progression


def ask_question_get_answer():
    seq_start = randint(1, 5)
    step = randint(2, 5)
    num_of_steps = 8
    progression_list = get_progression(seq_start, num_of_steps, step)
    secret_number = randint(0, 8)
    correct_answer = str(progression_list[secret_number])
    progression_list[secret_number] = '..'
    question = ' '.join(str(e) for e in progression_list)
    return question, correct_answer
