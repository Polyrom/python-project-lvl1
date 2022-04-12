from random import randint
import prompt


def get_progression(start, total_steps, difference):
    mylist = [start]
    i = 0
    while i <= total_steps:
        mylist.append(start + difference)
        start = start + difference
        i += 1
    return mylist


def run_brain_progression():
    print('Welcome to the Brain Games!')
    player = prompt.string("May I have your name? ")
    print("Hello, " + player)
    print('What number is missing in the progression?')
    index = 0
    while index < 3:
        seq_start = randint(1, 5)
        step = randint(2, 5)
        num_of_steps = 8
        progression_list = get_progression(seq_start, num_of_steps, step)
        secret_number = randint(0, 8)
        correct_answer = progression_list[secret_number]
        progression_list[secret_number] = '..'
        str1 = ' '.join(str(e) for e in progression_list)
        print(f'Question: {str1}')
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print("Correct!")
            index += 1
        else:
            return print(
                f'"{answer}" is wrong answer ;(. '
                f'The correct answer was "{correct_answer}".'
                f'\nLet\'s try again, {player}!')
    print("Congratulations, " + player + "!")
