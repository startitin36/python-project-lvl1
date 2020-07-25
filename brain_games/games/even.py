import prompt
from random import randint


name = ''
INTRO_EVEN = 'Answer "yes" if number even or answer "no"'
WRONG_MSG = 'is wrong answer ;(. Correct answer was'


def main(name):
    cor_ans = 0
    while cor_ans < 3:
        num = randint(1, 100)
        print('Question: {}'.format(num))
        ans = prompt.string('Your answer: ')
        if (num % 2 == 0 and ans == 'yes') or (num % 2 == 1 and ans == 'no'):
            print('Correct!')
            cor_ans += 1
        else:
            if ans == 'yes':
                show_ans = 'no'
            else:
                show_ans = 'yes'
            print("'{}' {} '{}'".format(ans, WRONG_MSG, show_ans))
            break
    return cor_ans


if __name__ == '__main__':
    print(INTRO_EVEN)
    main(name)
