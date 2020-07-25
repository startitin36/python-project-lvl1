#!/usr/bin/env python3


from brain_games.scripts.cli import welcome_user
import brain_games.games.even
import brain_games.games.calc
import brain_games.games.gcd
import brain_games.games.progress
import brain_games.games.isprime
import prompt


GREETING_MSG = 'Welcome to the Brain Games!'
CHOICE_MSG = 'Please,  choise your game by pressing suitable number:'
GAMES = '1. Even\n2. Calc\n3. GCD\n4. Progression\n5. IsPrime\n'


def main():
    print(GREETING_MSG, '\n')
    name = welcome_user()
    print(CHOICE_MSG, '\n')
    game = prompt.string(GAMES)
    cor_ans = 0
    if game == '1':
        print(brain_games.games.even.INTRO_EVEN, '\n')
        cor_ans = brain_games.games.even.main(name)
    elif game == '2':
        print(brain_games.games.calc.INTRO_CALC, '\n')
        cor_ans = brain_games.games.calc.main(name)
    elif game == '3':
        print(brain_games.games.gcd.INTRO_GCD, '\n')
        cor_ans = brain_games.games.gcd.main(name)
    elif game == '4':
        print(brain_games.games.progress.INTRO_PROGRESS, '\n')
        cor_ans = brain_games.games.progress.main(name)
    elif game == '5':
        print(brain_games.games.isprime.INTRO_PRIME, '\n')
        cor_ans = brain_games.games.isprime.main(name)
    else:
        print('Wrong input, {}. Try again!'.format(name))
    if cor_ans == 3:
        print('Congratulations, {}!'.format(name))
    else:
        print("Let's try again, {}!".format(name))


if __name__ == '__main__':
    main()
