from random import randint


INTRO = 'What number is missing in the progression?'


def progress():
    quest_str = ''
    start = randint(1, 100)
    step = randint(1, 10)
    mis_pos = randint(1, 10)
    numbers = 10
    count = 1
    while count <= numbers:
        next_num = start + step * (count - 1)
        if count == mis_pos:
            quest_str += ' ...'
            result = str(next_num)
        else:
            quest_str += ' ' + str(next_num)
        count += 1
    return (quest_str, result)
