import prompt
from random import randint


name = ''


def even(name):
    print('Answer "yes" if number even or answer "no"')
    cor_ans = 0
    while cor_ans < 3:
        num = randint(1, 100)
        print('Question: {}'.format(num))
        answ = prompt.string('Your answer: ')
        if (num % 2 == 0 and answ == 'yes') or (num % 2 == 1 and answ == 'no'):
            print('Correct!')
            cor_ans += 1
        else:
            if answ == 'yes':
                show_ans = 'no'
            else:
                show_ans = 'yes'
            print("'{}' is wrong answer ;(. Correct answer was '{}'".format(answ, show_ans))
            break
    return cor_ans


if __name__ == '__main__':
    even(name)
