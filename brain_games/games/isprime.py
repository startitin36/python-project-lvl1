from random import randint


INTRO = 'Answer "yes" if given number prime. Otherwise answer "no".'
START_NUM = 2
END_NUM = 100


def get_game_data():
    result = 'no'
    num = randint(START_NUM, END_NUM)
    question = str(num)
    if is_prime(num):
        result = 'yes'
    return (question, result)


def is_prime(num):
    if num % 2 == 0:
        return num == 2
    div = 3
    while div * div <= num and num % div != 0:
        div += 2
    return div * div > num
