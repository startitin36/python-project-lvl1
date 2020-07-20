#!/usr/bin/env python3


from brain_games.games.even import even, intro_even
from brain_games.scripts.cli import welcome_user


greeting_msg = 'Welcome to the Brain Games!'
win_msg = 'Congratulatins, {}!'
lose_msg = "Let's try again, {}!"


def main():
    print(greeting_msg, '\n')
    name = welcome_user()
    print(intro_even, '\n')
    cor_ans = even(name)
    if cor_ans == 3:
        print(win_msg.format(name))
    else:
        print(lose_msg.format(name))


if __name__ == '__main__':
    main()
