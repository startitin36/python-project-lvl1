import prompt
from random import randint


name = ''
intro_prime = 'Answer "yes" if given number prime. Otherwise answer "no".'
wrong_msg = 'is wrong answer ;(. Correct answer was'


def prime(name):
    cor_ans = 0
    while cor_ans < 3:
        num = randint(1, 100)
        print('Question: {}'.format(num))
        ans = prompt.string('Your answer: ')
        div = 3
        if ((num % 2 == 0 or num == 1) and ans == 'no'):
            print('Correct!')
            cor_ans += 1
        else:
            while div * div <= num and num % div != 0:
                div += 2
            if (div * div <= num or num % div == 0):
                show_ans = 'no'
            else:
                show_ans = 'yes'
            if ans == show_ans:
                print('Correct')
                cor_ans += 1
            else:
                if show_ans == 'yes':
                    print("'{}' {} '{}'".format(ans, wrong_msg, show_ans))
                else:
                    print("'{}' {} '{}'".format(ans, wrong_msg, show_ans))
                break
    return cor_ans


if __name__ == '__main__':
    print(intro_prime)
    prime(name)
