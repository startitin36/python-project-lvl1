from random import randint


INTRO = 'Answer "yes" if number even or answer "no"'


def even():
    num = randint(1, 100)
    quest_str = str(num)
    if num % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return (quest_str, str(result))
