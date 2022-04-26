import prompt


NUMBER_OF_ROUNDS = 3


def run(game):
    print('Welcome to the Brain Games!')
    player = prompt.string('May I have your name? ')
    print(f'Hello, {player}')
    print(game.GAME_RULES)
    for game_round in range(NUMBER_OF_ROUNDS):
        question, correct_answer = game.get_question_and_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(
                f'"{answer}" is wrong answer ;(. '
                f'The correct answer was "{correct_answer}".'
                f'\nLet\'s try again, {player}!')
            return
    print(f"Congratulations, {player}!")
