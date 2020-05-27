import prompt
from random import randint


name = ''


def even(name):
    cor_ans = 0
    while cor_ans < 3:
        num = randint(1, 100)
        print('Question: {}'.format(num))
        answ = prompt.string('Your answer: ')
        if (num % 2 == 0 and answ == 'yes') or (num % 2 == 1 and answ == 'no'):
            print('Correct!')
            cor_ans += 1
        else:
            print("'{}' is wrong answer ;(".format(answ))
            break
    if cor_ans == 3:
        print('Congratulations, {}!'.format(name))
    else:
        print("Let's try again, {}!".format(name))


if __name__ == '__main__':
    even(name)
