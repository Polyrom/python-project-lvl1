import prompt


def run_game(game_rules, ask_question_get_answer):
    print('Welcome to the Brain Games!')
    player = prompt.string('May I have your name? ')
    print('Hello, ' + player)
    print(game_rules)
    for game_round in range(3):
        question, correct_answer = ask_question_get_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            return print(
                f'"{answer}" is wrong answer ;(. '
                f'The correct answer was "{correct_answer}".'
                f'\nLet\'s try again, {player}!')
    print("Congratulations, " + player + "!")
