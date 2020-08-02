#!/usr/bin/env python3


from brain_games.scripts.cli import welcome_user


GREETING_MSG = 'Welcome to the Brain Games!'


def main():
    print(GREETING_MSG, '\n')
    welcome_user()


if __name__ == '__main__':
    main()
