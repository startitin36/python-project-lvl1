from random import randint


INTRO = 'What number is missing in the progression?'
START_NUM = 1
END_NUM = 100
STEP_TO = 10
MISSED_NUM_MIN_POS = 0
HIGHEST_NUM_POS = 9


def get_game_data():
    question = ''
    start = randint(START_NUM, END_NUM)
    step = randint(START_NUM, STEP_TO)
    mis_pos = randint(MISSED_NUM_MIN_POS, HIGHEST_NUM_POS)
    current_pos = 0
    while current_pos <= HIGHEST_NUM_POS:
        number = start + step * current_pos
        if current_pos in range(START_NUM, HIGHEST_NUM_POS + 1):
            question += ' '
        if current_pos == mis_pos:
            question += '...'
            result = str(number)
        else:
            question += str(number)
        current_pos += 1
    return (question, result)
