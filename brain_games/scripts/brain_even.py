#!/usr/bin/env python3


from brain_games.even import even
from brain_games.scripts.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even or answer "no".\n')
    name = welcome_user()
    even(name)


if __name__ == '__main__':
    main()
