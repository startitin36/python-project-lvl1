from random import randint
from random import choice


INTRO = 'What is the result of the expression?'


def calc():
    operations = ['*', '+', '-']
    n1 = randint(1, 100)
    n2 = randint(1, 100)
    operation = choice(operations)
    quest_str = str(n1) + ' ' + operation + ' ' + str(n2)
    if operation == '*':
        result = n1 * n2
    elif operation == '+':
        result = n1 + n2
    else:
        result = n1 - n2
    return (quest_str, str(result))
