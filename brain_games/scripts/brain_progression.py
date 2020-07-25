#!/usr/bin/env python3


import brain_games.games.progress
from brain_games.scripts.cli import welcome_user


GREETING_MSG = 'Welcome to the Brain Games!'
WIN_MSG = 'Congratulatins, {}!'
LOSE_MSG = "Let's try again, {}!"


def main():
    print(GREETING_MSG, '\n')
    name = welcome_user()
    print(brain_games.games.progress.INTRO_PROGRESS, '\n')
    cor_ans = brain_games.games.progress.main(name)
    if cor_ans == 3:
        print(WIN_MSG.format(name))
    else:
        print(LOSE_MSG.format(name))


if __name__ == '__main__':
    main()
