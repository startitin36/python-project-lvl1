from random import randint


INTRO = 'Answer "yes" if given number prime. Otherwise answer "no".'
LIMIT_OF_AREA = 100


def get_game_data():
    result = ''
    num = randint(-LIMIT_OF_AREA, LIMIT_OF_AREA)
    question = str(num)
    if is_prime(num):
        result = 'yes'
    else:
        result = 'no'
    return (question, result)


def is_prime(num):
    if num < 2:
        return False
    if num % 2 == 0:
        return num == 2
    div = 3
    while num % div != 0:
        if div * div > num:
            return True
        div += 2
    return False
