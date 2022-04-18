from random import randint


def get_progression(start, total_steps, difference):
    mylist = [start]
    i = 0
    while i <= total_steps:
        mylist.append(start + difference)
        start = start + difference
        i += 1
    return mylist


def ask_question():
    seq_start = randint(1, 5)
    step = randint(2, 5)
    num_of_steps = 8
    progression_list = get_progression(seq_start, num_of_steps, step)
    secret_number = randint(0, 8)
    global cor_ans
    cor_ans = str(progression_list[secret_number])
    progression_list[secret_number] = '..'
    question_string = ' '.join(str(e) for e in progression_list)
    print(f'Question: {question_string}')


def get_correct_answer():
    correct_answer = cor_ans
    return correct_answer
