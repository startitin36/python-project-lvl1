from random import randint


INTRO = 'Answer "yes" if given number prime. Otherwise answer "no".'


def isprime():
    num = randint(1, 100)
    div = 3
    quest_str = str(num)
    if num == 2:
        result = 'yes'
    elif (num % 2 == 0 or num == 1):
        result = 'no'
    else:
        while div * div <= num and num % div != 0:
            div += 2
            if (div * div <= num or num % div == 0):
                result = 'no'
            else:
                result = 'yes'
    return (quest_str, result)
