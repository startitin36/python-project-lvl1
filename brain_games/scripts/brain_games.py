#!/usr/bin/env python3


from brain_games.scripts.cli import welcome_user
import brain_games.games.even
import brain_games.games.calc
import brain_games.games.gcd
import brain_games.games.progress
import brain_games.games.isprime
import prompt


greeting_msg = 'Welcome to the Brain Games!'
choice_msg = 'Please,  choise your game by pressing suitable number:'
games = '1. Even\n2. Calc\n3. GCD\n4. Progression\n5. IsPrime\n'


def main():
    print(greeting_msg, '\n')
    name = welcome_user()
    print(choice_msg, '\n')
    game = prompt.string(games)
    cor_ans = 0
    if game == '1':
        print(brain_games.games.even.intro_even, '\n')
        cor_ans = brain_games.games.even.even(name)
    elif game == '2':
        print(brain_games.games.calc.intro_calc, '\n')
        cor_ans = brain_games.games.calc.calc(name)
    elif game == '3':
        print(brain_games.games.gcd.intro_gcd, '\n')
        cor_ans = brain_games.games.gcd.gcd_game(name)
    elif game == '4':
        print(brain_games.games.progress.intro_progress, '\n')
        cor_ans = brain_games.games.progress.progress(name)
    elif game == '5':
        print(brain_games.games.isprime.intro_prime, '\n')
        cor_ans = brain_games.games.isprime.prime(name)
    else:
        print('Wrong input, {}. Try again!'.format(name))
    if cor_ans == 3:
        print('Congratulations, {}!'.format(name))
    else:
        print("Let's try again, {}!".format(name))


if __name__ == '__main__':
    main()
