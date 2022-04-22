#!/usr/bin/env python

from brain_games.engine import run_game
from brain_games.games.gcd import game_rules, ask_question_get_answer


def main():
    run_game(game_rules, ask_question_get_answer)


if __name__ == "__main__":
    main()
