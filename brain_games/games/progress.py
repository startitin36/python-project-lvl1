from random import randint


INTRO = 'What number is missing in the progression?'
START_NUM = 1
END_NUM = 100
STEP_TO = 10
MIS_NUM_MIN_POS = 1
MIS_NUM_MAX_POS = 10
NUM_OF_NUMS = 10


def main():
    question = ''
    start = randint(START_NUM, END_NUM)
    step = randint(START_NUM, STEP_TO)
    mis_pos = randint(MIS_NUM_MIN_POS, MIS_NUM_MAX_POS)
    count = 1
    while count <= NUM_OF_NUMS:
        next_num = start + step * (count - 1)
        if count == mis_pos:
            question += ' ...'
            result = str(next_num)
        else:
            question += ' ' + str(next_num)
        count += 1
    return (question, result)
