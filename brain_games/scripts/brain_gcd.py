#!/usr/bin/env python3


import brain_games.games.gcd
from brain_games.scripts.cli import welcome_user


GREETING_MSG = 'Welcome to the Brain Games!'
WIN_MSG = 'Congratulations, {}!'
LOSE_MSG = "Let's try again, {}!"


def main():
    print(GREETING_MSG, '\n')
    name = welcome_user()
    print(brain_games.games.gcd.INTRO_GCD, '\n')
    cor_ans = brain_games.games.gcd.main(name)
    if cor_ans == 3:
        print(WIN_MSG.format(name))
    else:
        print(LOSE_MSG.format(name))


if __name__ == '__main__':
    main()
