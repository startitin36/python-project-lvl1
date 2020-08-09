from random import randint
from math import gcd


INTRO = 'Find the greatest common divisor of given numbers.'
START_NUM = 1
END_NUM = 100


def main():
    n1 = randint(START_NUM, END_NUM)
    n2 = randint(START_NUM, END_NUM)
    question = str(n1) + ' ' + str(n2)
    result = str(gcd(n1, n2))
    return (question, result)
