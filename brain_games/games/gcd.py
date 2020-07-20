import prompt
from random import randint
from math import gcd


name = ''


intro_gcd = 'Find the greatest common divisor of given numbers'


def gcd_game(name):
    cor_ans = 0
    wrong_msg = 'is wrong answer ;(. Correct answer was'
    while cor_ans < 3:
        n1 = randint(1, 100)
        n2 = randint(1, 100)
        print('Question: {} {}'.format(n1, n2))
        answ = prompt.string('Your answer: ')
        if (gcd(n1, n2) == int(answ)):
            print('Correct!')
            cor_ans += 1
        else:
            print("'{}' {} '{}'".format(answ, wrong_msg, gcd(n1, n2)))
            break
    return cor_ans


if __name__ == '__main__':
    print(intro_gcd)
    gcd_game(name)
