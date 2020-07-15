#!/usr/bin/env python3


from brain_games.scripts.cli import welcome_user
from brain_games.games.even import even
from brain_games.games.calc import calc
import prompt

name = ''


def main():
    print('Welcome to the Brain Games!\n')
    name = welcome_user()
    print('Please,  choise your game by pressing suitable number:\n')
    game = prompt.string('1. Brain-even\n2. Brain-calc\n3. in progress...\n')
    cor_ans = 0
    if game == '1':
        cor_ans = even(name)
    elif game == '2':
        cor_ans = calc(name)
    elif game == '3':
        print('Will be ready soon... Stay tuned :)')
    else:
        print('Wrong input, {}. Try again!'.format(name))
    if cor_ans == 3:
        print('Congratulations, {}!'.format(name))
    else:
        print("Let's try again, {}!".format(name))


if __name__ == '__main__':
    main()
