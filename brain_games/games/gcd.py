from random import randint
from math import gcd


INTRO = 'Find the greatest common divisor of given numbers.'


def gcd_game():
    n1 = randint(1, 100)
    n2 = randint(1, 100)
    qest_str = str(n1) + ' ' + str(n2)
    result = str(gcd(n1, n2))
    return (qest_str, result)
