import prompt
from random import randint


name = ''
intro_progress = 'What number is missing in the progression?'


def progress(name):
    cor_ans = 0
    wrong_msg = 'is wrong answer :(. Correct answer was'
    mis_num = '..'
    while cor_ans < 3:
        quest_str = ''
        start = randint(1, 100)
        step = randint(1, 10)
        mis_pos = randint(1, 10)
        numbers = 10
        count = 1
        while count <= numbers:
            next_num = start + step * (count - 1)
            if count == mis_pos:
                quest_str += ' ' + mis_num
                correct = next_num
            else:
                quest_str += ' ' + str(next_num)
            count += 1
        print(quest_str)
        ans = prompt.string('Your answer: ')
        if str(correct) == ans:
            print('Correct!')
            cor_ans += 1
        else:
            print("'{}' {} '{}'".format(ans, wrong_msg, correct))
            break
    return cor_ans


if __name__ == '__main__':
    progress(name)
