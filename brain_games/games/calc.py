import prompt
from random import randint
from random import choice

name = ''


def calc(name):
    cor_ans = 0
    operations = ['multiple', 'addition']
    wrong_msg = 'is wrong answer :(. Correct answer was'
    while cor_ans < 3:
        n1 = randint(1, 100)
        n2 = randint(1, 100)
        operation = choice(operations)
        if operation == 'multiple':
            print('Question: {} * {}'.format(n1, n2))
            ans = prompt.string('Your answer: ')
            if ((n1 * n2) == int(ans)):
                print('Correct!')
                cor_ans += 1
            else:
                print("'{}' {} '{}'".format(ans, wrong_msg, n1 * n2))
                break
        else:
            print('Question: {} + {}'.format(n1, n2))
            ans = prompt.string('Your answer: ')
            if ((n1 + n2) == int(ans)):
                print('Correct!')
                cor_ans += 1
            else:
                print("'{}' {} '{}'.".format(ans, wrong_msg, n1 + n2))
                break
    return cor_ans


if __name__ == '__main__':
    calc(name)
