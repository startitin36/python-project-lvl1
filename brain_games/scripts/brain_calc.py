#!/usr/bin/env python3


from brain_games.games.calc import calc
from brain_games.scripts.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    print('What is the result of expression?\n')
    name = welcome_user()
    calc(name)


if __name__ == '__main__':
    main()
