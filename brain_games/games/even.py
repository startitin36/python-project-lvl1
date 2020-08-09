from random import randint


INTRO = 'Answer "yes" if number even or answer "no"'


def main():
    num = randint(1, 100)
    question = str(num)
    if num % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return (question, str(result))
