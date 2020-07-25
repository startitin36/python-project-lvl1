import prompt
from random import randint
from math import gcd


name = ''
INTRO_GCD = 'Find the greatest common divisor of given numbers'
WRONG_MSG = 'is wrong answer ;(. Correct answer was'


def main(name):
    cor_ans = 0
    while cor_ans < 3:
        n1 = randint(1, 100)
        n2 = randint(1, 100)
        print('Question: {} {}'.format(n1, n2))
        ans = prompt.string('Your answer: ')
        if (gcd(n1, n2) == int(ans)):
            print('Correct!')
            cor_ans += 1
        else:
            print("'{}' {} '{}'".format(ans, WRONG_MSG, gcd(n1, n2)))
            break
    return cor_ans


if __name__ == '__main__':
    print(INTRO_GCD)
    main(name)
