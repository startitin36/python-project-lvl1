import prompt
from random import randint
from random import choice

name = ''


def calc(name):
    cor_ans = 0
    operations = ['multiple', 'addition']
    while cor_ans < 3:
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        operation = choice(operations)
        if operation == 'multiple':
            print('Question: {} * {}'.format(num1, num2))
            answ = prompt.string('Your answer: ')
            if ((num1 * num2) == int(answ)):
                print('Correct!')
                cor_ans += 1
            else:
                print("'{}' is wrong answer ;(. Correct answer was '{}'".format(answ, (num1 * num2)))  
                break
        else:
            print('Question: {} + {}'.format(num1, num2))
            answ = prompt.string('Your answer: ')
            if ((num1 + num2) == int(answ)):
                print('Correct!')
                cor_ans += 1
            else:
                print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answ, (num1 + num2)))
                break
    return cor_ans 

if __name__ == '__main__':
    calc(name)
